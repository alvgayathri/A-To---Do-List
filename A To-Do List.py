def display_tasks(tasks):
    if not tasks:
        print("No tasks available.")
    else:
        print("\nYour To-Do List:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def add_task(tasks):
    task = input("Enter task: ")
    tasks.append(task)
    print("Task added successfully!")

def remove_task(tasks):
    display_tasks(tasks)
    try:
        index = int(input("Enter task number to remove: ")) - 1
        if 0 <= index < len(tasks):
            removed = tasks.pop(index)
            print(f"Removed task: {removed}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def save_tasks(tasks, filename="tasks.txt"):
    with open(filename, "w") as file:
        for task in tasks:
            file.write(task + "\n")
    print("Tasks saved successfully!")

def load_tasks(filename="tasks.txt"):
    try:
        with open(filename, "r") as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        return []

def main():
    tasks = load_tasks()
    while True:
        print("\nOptions: 1. Add 2. Remove 3. View 4. Save & Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            remove_task(tasks)
        elif choice == "3":
            display_tasks(tasks)
        elif choice == "4":
            save_tasks(tasks)
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
