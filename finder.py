# Simple To-Do List App

tasks = []

def show_tasks():
    if not tasks:
        print("\nNo tasks yet!\n")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
        print()

while True:
    print("=== TO-DO LIST MENU ===")
    print("1. Add task")
    print("2. View tasks")
    print("3. Remove task")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        task = input("Enter a new task: ")
        tasks.append(task)
        print("Task added!\n")

    elif choice == "2":
        show_tasks()

    elif choice == "3":
        show_tasks()
        try:
            num = int(input("Enter task number to remove: "))
            removed = tasks.pop(num - 1)
            print(f"Removed: {removed}\n")
        except:
            print("Invalid choice!\n")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid option, try again.\n")