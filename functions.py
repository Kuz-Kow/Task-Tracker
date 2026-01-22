from email.mime import text
import json
from operator import index
import task_class as task
import os
import time

def delete():
    pass


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


    
    

def list():
    with open('data.json', 'r') as f:
        data = json.load(f)

        if not data:
            print("No data found.")
            return
    
    for item in data:
        print(f"ID: {item['id']}, Description: {item['description']}, Status: {item['completed']}, Created At: {item['created_at']}, Updated At: {item['updated_at']}")


def mark_in_progress():
    pass

def mark_done():
    pass