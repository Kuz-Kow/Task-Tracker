import argparse
import json
import datetime
from pathlib import Path
import functools
from typing import TypedDict, Literal, Callable

DATA_PATH = Path("data.json")

type data_base = dict[str, Field]


class Field(TypedDict):
    description: str
    status: Literal["todo", "done", "in-progress"]
    created_at: str
    updated_at: str


def main() -> None:
    args = vars(parser.parse_args())
    function = args.pop("func")
    function(**args)


def data(func: Callable):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        data = get_data()
        result = func(data, *args, **kwargs)
        store_data(data)
        return result

    return wrapper


def get_data() -> data_base:
    """
    Get's data from file
    """

    try:
        with DATA_PATH.open("r", encoding="utf-8") as file:
            data: data_base = json.load(file)
            return data
    except FileNotFoundError:
        return {}


def store_data(data: data_base) -> None:
    """
    Stores data in the file
    """

    with DATA_PATH.open("w", encoding="utf-8") as file:
        json.dump(data, file, indent=2)


@data
def add(data: data_base, text: str) -> None:
    """
    Adds new record to the data base
    """

    today: str = datetime.date.today().strftime("%Y-%m-%d %H:%M:%S")
    new_id = max(map(int, data), default=0) + 1
    data[str(len(data.keys()) + 1)] = {
        "description": text,
        "status": "todo",
        "created_at": today,
        "updated_at": today,
    }
    print(f"Task added successfully (ID :{new_id})")


@data
def update(data: data_base, id: str, text: str) -> None:
    """
    Updates existing record with new description.
    If id of the record not in the data base KeyError raiesed.
    """

    today = datetime.date.today().strftime("%Y-%m-%d %H:%M:%S")
    if id in data:
        data[id]["description"] = text
        data[id]["updated_at"] = today
    else:
        raise KeyError("There no task with this id")


@data
def delete(data: data_base, id: str) -> None:
    """
    Deletes record from the data base.
    If id of the record not in the data base KeyError raiesed.
    """

    if id in data:
        del data[id]
    else:
        raise KeyError("There no task with this id")


def list_tasks(progress: Literal["todo", "done", "in-progress"] | None) -> None:
    """
    Lists tasks with status provieded as a progress argument.
    If no rogress argument was provided lists all task.
    """

    db = get_data()
    for id, fields in db.items():
        if progress is None or fields["status"] == progress:
            print(f"\nid : {id}")
            for field in fields.items():
                print(f"{field[0]} : {field[1]}")


@data
def mark_in_progress(data: data_base, id: str):
    """
    Mark existing task in the data base as in-progress.
    If id of the record not in the data base KeyError raiesed.
    """

    today: str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if id in data:
        data[id]["status"] = "in-progress"
        data[id]["updated_at"] = today
    else:
        raise KeyError("There no task with this id")


@data
def mark_done(data: data_base, id: str):
    """
    Marks existing task in the data base as done.
    If id of the record not in the data base KeyError raiesed.
    """

    today: str = datetime.date.today().strftime("%Y-%m-%d %H:%M:%S")
    if id in data:
        data[id]["status"] = "done"
        data[id]["updated_at"] = today
    else:
        raise KeyError("There no task with this id")


parser = argparse.ArgumentParser(
    prog="Task-Tracker-CLI",
    description="Task Tracker CLI is a simple command-line application for managing tasks. It allows you to add, update, delete, and track the status of your tasks. All tasks are stored in a local JSON file in the current directory.",
)


subparsers = parser.add_subparsers(required=True)

add_parser = subparsers.add_parser("add", help="Add a new task")
add_parser.add_argument(
    "text", type=str, help="Description of the task", action="store"
)
add_parser.set_defaults(func=add)


update_parser = subparsers.add_parser("update", help="Update an existing task")
update_parser.add_argument(
    "id", type=str, help="Task ID to update the task", action="store"
)
update_parser.add_argument(
    "text",
    type=str,
)
update_parser.set_defaults(func=update)


delete_parser = subparsers.add_parser("delete", help="Delete a task by ID")
delete_parser.add_argument(dest="id", type=str, help="ID of the task to delete()")
delete_parser.set_defaults(func=delete)


list_parser = subparsers.add_parser("list", help="List tasks (optionally by status)")
list_parser.add_argument(
    dest="progress",
    type=str,
    default=None,
    nargs="?",
    choices=["done", "todo", "in-progress"],
)

list_parser.set_defaults(func=list_tasks)


mark_in_progress_parser = subparsers.add_parser(
    "mark-in-progress", help="Filter by status: todo, in-progress, done"
)
mark_in_progress_parser.add_argument(dest="id", type=str, help="ID of the task")
mark_in_progress_parser.set_defaults(func=mark_in_progress)

mark_done_parser = subparsers.add_parser("mark-done", help="Mark a task as done")
mark_done_parser.add_argument(dest="id", type=str, help="ID of the task")
mark_done_parser.set_defaults(func=mark_done)


if __name__ == "__main__":
    main()
