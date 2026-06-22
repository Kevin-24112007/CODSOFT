tasks = []
def view_tasks(tasks):
    if len(tasks) == 0:
        print("No tasks found.")
    else:
        print("\nYour tasks:")
        for i,task in enumerate(tasks):
            print(f"{i+1}. {task}")

def add_tasks(tasks):
    task = input("Enter your task: ")
    tasks.append(task)
    print("Task added!")

def remove_tasks(tasks):
    if len(tasks) == 0:
        print("No tasks found.")
        return
    view_tasks(tasks)
    try:
        task_num = int(input("Enter task number to remove: "))
        if 1 <= task_num <= len(tasks):
            removed = tasks.pop(task_num - 1)
            print(f"'{removed}' removed successfully!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

while True:
    print("\n----------TO-DO LIST MENU----------")
    print("1. View tasks\n2. Add tasks\n3. Remove tasks\n4. Exit\n")

    ch = int(input("Enter your choice: "))
    if ch == 1:
        view_tasks(tasks)
    elif ch == 2:
        add_tasks(tasks)
    elif ch == 3:
        remove_tasks(tasks)
    elif ch == 4:
        print("Thank you for using the TO-DO LIST")
        break
    else:
        print("Invalid choice.")