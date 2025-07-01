def display_menu():
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Quit")

def add_task(tasks):
    task = input("Enter task: ")
    tasks.append(task)

def view_tasks(tasks):
    if not tasks:
        print("No tasks added.")
        return
    for index, task in enumerate(tasks, 1):
        print(f"{index}. {task}")

def main():
    tasks = []
    while True:
        display_menu()
        choice = input("Choose option: ")
        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            print("Exiting. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
