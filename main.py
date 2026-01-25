import task_class as task
import argparse
import json
import task_class as task
import os
import time





def add(text):
    new_task = task.task(text)

    new_task_data = {
            "id": new_task.id,
            "description": new_task.description,
            "completed": "todo",
            "created_at": new_task.created_at,
            "updated_at": new_task.updated_at
        }


    if os.path.exists("data.json"):
        with open("data.json", "r") as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                data = []
    else:
        data = []


    new_task_data["id"] = data[-1]["id"] + 1 if data else 1
    new_task.id = new_task_data["id"]

    data.append(new_task_data)


    with open("data.json", "w") as f:
        json.dump(data, f, indent=4)

    print(f"Added task: {text} with ID {new_task_data['id']}")




def update(task_id, text):
    with open('data.json', 'r') as f:
        data = json.load(f)

        if not data:
            print("No data found.")
            return

    index = int(task_id) - 1


    data[index]["description"] = text
    data[index]["updated_at"] = time.asctime()


    with open("data.json", "w") as f:
        json.dump(data, f, indent=4)


        
    

def list_tasks(progress):

    
    with open('data.json', 'r') as f:
        data = json.load(f)

    if not data:
        print("No data found.")
        return
    
    if progress == None:
            
        for item in data:
            print(f"ID: {item['id']}, Description: {item['description']}, Status: {item['completed']}, Created At: {item['created_at']}, Updated At: {item['updated_at']}")
    else:
        for item in data:
            if item["completed"] == progress:
                print(f"ID: {item['id']}, Description: {item['description']}, Status: {item['completed']}, Created At: {item['created_at']}, Updated At: {item['updated_at']}")


def delete(task_id):
    if os.path.exists("data.json"):
        with open("data.json", "r") as f:
            try: 
                data = json.load(f)
            except json.JSONDecodeError:
                data = []

    else:
        print("There is no database")


    index = int(task_id) - 1


    del data[index]

    with open("data.json", "w") as f:
        json.dump(data, f, indent=4)

    print("Pomyślnie usunięto zapis")



def mark_in_progress(task_id):
    if os.path.exists("data.json"):
        with open("data.json", "r") as f:
            try: 
                data = json.load(f)
            except json.JSONDecodeError:
                data = []

    else:
        print("There is no database")


    index = int(task_id) - 1


    data[index]["completed"] = "in-progress"
    data[index]["updated_at"] = time.asctime()

    with open("data.json", "w") as f:
        json.dump(data, f, indent=4)


def mark_done(task_id):
    if os.path.exists("data.json"):
        with open("data.json", "r") as f:
            try: 
                data = json.load(f)
            except json.JSONDecodeError:
                data = []

    else:
        print("There is no database")


    index = int(task_id) - 1


    data[index]["completed"] = "done"
    data[index]["updated_at"] = time.asctime()

    with open("data.json", "w") as f:
        json.dump(data, f, indent=4)





parser = argparse.ArgumentParser()


subparsers = parser.add_subparsers(dest= "command", required= True)
add_parser = subparsers.add_parser('add', help='...')
add_parser.add_argument('Task_text', type=str, help='...', action='store')



update_parser = subparsers.add_parser('update', help='...')
update_parser.add_argument( metavar=("TASK_ID", "TEXT"), type=str, help='...', nargs=2, dest='update_task', action='store')



delete_parser = subparsers.add_parser('delete', help='...')
delete_parser.add_argument( dest="delete_task", type=str, help='...')




list_parser = subparsers.add_parser('list', help='...')
list_parser.add_argument(dest = 'progress', type=str ,default=None)

mark_in_progress_parser = subparsers.add_parser('mark-in-progress', help='...')
mark_in_progress_parser.add_argument( dest="mark_in_progress", type=str, help='...')

mark_in_done_parser = subparsers.add_parser('mark-done', help='...')
mark_in_done_parser.add_argument( dest="mark_done", type=str, help='...')








args = parser.parse_args()

if args.command == 'list':
    list_tasks(args.progress)


if args.command == 'add':
    add(args.Task_text)

if args.command == 'update':
    update(args.update_task[0], args.update_task[1])

if args.command == 'delete':
    delete(args.delete_task)

if args.command == 'mark-in-progress':
    mark_in_progress(args.mark_in_progress)

if args.command == 'mark-done':
    mark_done(args.mark_done)

if args.command == 'mark-done':
    pass














