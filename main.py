import task_class as task
import argparse
import functions
import json


parser = argparse.ArgumentParser()
chioses = parser.add_mutually_exclusive_group()

chioses.add_argument("-a", "--add", type=str, help="Add a new task")
chioses.add_argument("-u", "--update",metavar=("TASK_ID", "TEXT"), type=str, help="Update an existing task", nargs=2)

chioses.add_argument("-d", "--delete", action="store_true", help="Delete a task")

chioses.add_argument("-l", "--list", action="store_true", help="List all tasks")

chioses.add_argument("-mip", "--mark_in_progress", metavar=("TASK_ID"),type = int, help="Mark task as in progress")

chioses.add_argument("-md", "--mark_done",metavar=("TASK_ID"),type= int, help="Mark task as done")



args = parser.parse_args()


if args.add is not None:
    functions.add(args.add)

elif args.update is not None:
    functions.update(args.update[0], args.update[1])


elif args.mark_done:
    functions.mark_done(args.mark_done) 

elif args.mark_in_progress:
    functions.mark_in_progress(args.mark_in_progress)

elif args.delete:
    functions.delete()

elif args.list:
    functions.list()








