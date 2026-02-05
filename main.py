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

    if index > len(data):
        print(f"Theres no item with index {task_id}")
        return

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

    if int(task_id) > len(data):
        print(f"Theres no item with index {task_id}")
        return


    index = int(task_id) - 1



    del data[index]

    for i in range (index, len(data)):
        data[i]["id"] = data[i]["id"] - 1

    with open("data.json", "w") as f:
        json.dump(data, f, indent=4)

    print(f"Item with id {task_id} has been deleted")



def mark_in_progress(task_id):
    if os.path.exists("data.json"):
        with open("data.json", "r") as f:
            try: 
                data = json.load(f)
            except json.JSONDecodeError:
                data = []

    else:
        print("There is no database")
    
    if int(task_id) > len(data):
        print(f"Theres no item with index {task_id}")
        return


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

    if int(task_id) > len(data):
        print(f"Theres no item with index {task_id}")
        return


    index = int(task_id) - 1


    data[index]["completed"] = "done"
    data[index]["updated_at"] = time.asctime()

    with open("data.json", "w") as f:
        json.dump(data, f, indent=4)





parser = argparse.ArgumentParser(prog='Task-Tracker-CLI', description='Task Tracker CLI is a simple command-line application for managing tasks. It allows you to add, update, delete, and track the status of your tasks. All tasks are stored in a local JSON file in the current directory.')


subparsers = parser.add_subparsers(dest= "command", required= True)
add_parser = subparsers.add_parser('add', help='Add a new task')
add_parser.add_argument('Task_text', type=str, help='Description of the task', action='store')



update_parser = subparsers.add_parser('update', help='Update an existing task')
update_parser.add_argument( metavar=("TASK_ID", "TEXT"), type=str, help='Task ID and new description', nargs=2, dest='update_task', action='store')



delete_parser = subparsers.add_parser('delete', help='Delete a task by ID')
delete_parser.add_argument( dest="delete_task", type=str, help='ID of the task to delete()')




list_parser = subparsers.add_parser('list', help='List tasks (optionally by status)')
list_parser.add_argument(dest = 'progress', type=str ,default=None)

mark_in_progress_parser = subparsers.add_parser('mark-in-progress', help='Filter by status: todo, in-progress, done')
mark_in_progress_parser.add_argument( dest="mark_in_progress", type=str, help='ID of the task')

mark_in_done_parser = subparsers.add_parser('mark-done', help='Mark a task as done')
mark_in_done_parser.add_argument( dest="mark_done", type=str, help='ID of the task')








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















