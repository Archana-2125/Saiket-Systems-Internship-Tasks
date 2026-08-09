tasks = []

while True:
    print("\n===== TO-DO LIST =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Exit")

    choice = input("Enter your choice: ")

    # Add Task
    if choice == "1":
        description = input("Enter task description: ")

        task = {
            "description": description,
            "completed": False
        }

        tasks.append(task)
        print("Task added successfully")
    # View Tasks
    elif choice == "2":
        if not tasks:
            print("No tasks available.")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, start=1):
                status = "Completed" if task["completed"] else "Pending"
                print(f"{i}. {task['description']} - {status}")

    # Mark Task as Completed
    elif choice == "3":
        if not tasks:
            print("No tasks available.")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, start=1):
                status = "Completed" if task["completed"] else "Pending"
                print(f"{i}. {task['description']} - {status}")

            task_number = int(input("Enter task number to mark as completed: "))

            if 1 <= task_number <= len(tasks):
                tasks[task_number - 1]["completed"] = True
                print("Task marked as completed")
            else:
                print("Invalid task number.")

    # Exit
    elif choice == "4":
        print("Thank you for using the To-Do List Application")
        break

    # Invalid Choice
    else:
        print("Invalid choice! Please try again.")
