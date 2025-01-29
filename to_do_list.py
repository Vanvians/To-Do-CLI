import os

TASKS_FILE = "tasks.txt"

def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            return [line.strip() for line in file.readlines()]
    return []

def save_tasks():
    with open(TASKS_FILE, "w") as file:
        for task in tasks:
            file.write(f"{task}\n")
    print("Tasks saved to file.")

def add_tasks(task):
    tasks.append(task)
    print(f"task added: {task}")
    save_tasks()

def view_tasks():
    if not tasks:
        print("No tasks available.")
    else:
        print("\nTo-Do List")
        for index, task in enumerate(tasks,start=1):
            print(f"{index}.{task}")

def delete_task(task_number):
    if 1 <= task_number <= len(tasks):
        removed = tasks.pop(task_number - 1)
        print(f"Removed task: {removed}")
    else:
        print("Invalid task number.")

    save_tasks()

def delete_all_tasks():
    global tasks
    tasks.clear()
    print("All tasks have been deleted")
    save_tasks()

def main():
    while True:
        print("\nOptions: add | view | delete | delete all | exit")
        choice = input("Enter command: ").strip().lower()
        
        if choice == "add":
            task = input("Enter task: ").strip()
            add_tasks(task)
        elif choice == "view":
            view_tasks()
        elif choice == "delete":
            view_tasks()
            try:
                task_number = int(input("Enter task number to delete: "))
                delete_task(task_number)
            except ValueError:
                print("Invalid input! please enter a number.")
        elif choice == "delete all":
            delete_all_tasks()
        elif choice == "exit":
            print("Goodbye!")
            break
        else:
            print("Invalid command! Try again.")

if __name__ == "__main__":
    tasks = load_tasks()
    main()