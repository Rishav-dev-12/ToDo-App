def add_task(tasks):
    try:
        num_tasks = int(input("Enter the number of tasks you want to add: "))
        for i in range(num_tasks):
            task_name = input("Enter task: ")
            tasks.append(task_name)
        print(f"{num_tasks} tasks have been successfully added!\n")
    except ValueError:
        print("Invalid input! Please enter a valid number.\n")


def update_task(tasks):
    task_name = input("Enter the task name to be updated: ")
    if task_name in tasks:
        new_task_name = input("Enter the new task name: ")
        tasks[tasks.index(task_name)] = new_task_name
        print(f"Task '{task_name}' updated to '{new_task_name}' successfully!\n")
    else:
        print("Task not found!\n")

def delete_task(tasks):
    task_name = input("Enter the task name to delete: ")
    if task_name in tasks:
        tasks.remove(task_name)
        print(f"Task '{task_name}' has been deleted successfully!\n")
    else:
        print("Task not found!\n")

def view_tasks(tasks):
    if tasks:
        print("\nYour Current Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
    else:
        print("\nNo tasks available!\n")

def task_manager():
    tasks = []  # Task list
    print("---- WELCOME TO THE PYTHON TO-DO APPLICATION ----")
    
    while True:
        try:
            operation = int(input("\nChoose an option:\n1-Add\n2-Update\n3-Delete\n4-View\n5-Exit\n"))
            if operation == 1:
                add_task(tasks)
            elif operation == 2:
                update_task(tasks)
            elif operation == 3:
                delete_task(tasks)
            elif operation == 4:
                view_tasks(tasks)
            elif operation == 5:
                print("Exiting the program...")
                break
            else:
                print("Invalid option! Please enter a number between 1 and 5.\n")
        except ValueError:
            print("Invalid input! Please enter a valid number.\n")

# Run the To-Do application
task_manager()
