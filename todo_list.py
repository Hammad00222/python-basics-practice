tasks = []

def show_menu():
    print("\nTo-Do List Menu:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Done")
    print("4. Delete Task")
    print("5. Exit")

def add_task():
    task = input("Enter a new task: ")
    tasks.append({"task": task, "done": False})
    print("Task added!")

def view_tasks():
    if not tasks:
        print("No tasks to show.")
        return
    print("\nYour Tasks:")
    for idx, task in enumerate(tasks, 1):
        status = "Done" if task["done"] else "Not Done"
        print(f"{idx}. {task['task']} [{status}]")

def mark_done():
    view_tasks()
    try:
        index = int(input("Enter task number to mark as done: "))
        if 1 <= index <= len(tasks):
            tasks[index - 1]["done"] = True
            print("Task marked as done!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a number.")

def delete_task():
    view_tasks()
    try:
        index = int(input("Enter task number to delete: "))
        if 1 <= index <= len(tasks):
            deleted = tasks.pop(index - 1)
            print(f"Task '{deleted['task']}' deleted!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a number.")

print("Welcome to the Python To-Do List!")

while True:
    show_menu()
    choice = input("Choose an option (1-5): ")

    if choice == '1':
        add_task()
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        mark_done()
    elif choice == '4':
        delete_task()
    elif choice == '5':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
