# Task-Tracker
Task Tracker CLI

Task Tracker CLI is a simple command-line application for managing tasks. It allows you to add, update, delete, and track the status of your tasks. All tasks are stored in a local JSON file in the current directory.

This project was built as a practice exercise for working with the file system, handling command-line arguments, and building a basic CLI tool without external libraries.

Features

The application supports the following actions:

  Add a new task

  Update an existing task

  Delete a task

  Mark a task as in-progress

  Mark a task as done

  List all tasks

  List tasks by status:

    todo

    in-progress

    done

Task Properties

  Each task has the following properties:

    id – Unique identifier

    description – Short task description

    status – todo, in-progress, or done

    createdAt – Date and time when the task was created

    updatedAt – Date and time when the task was last updated


Usage

  All commands are run from the terminal using positional arguments.

    Add a new task
    main add "Buy groceries"

    Update a task
    main update 1 "Buy groceries and cook dinner"

    Delete a task
    main delete 1

    Mark task as in progress
    main mark-in-progress 1

    Mark task as done
    main mark-done 1

    List all tasks
    main list

    List tasks by status
    main list todo
    main list in-progress
    main list done

Data Storage

  All tasks are stored in a file called:

  data.json


The file is automatically created in the current directory if it does not exist.
