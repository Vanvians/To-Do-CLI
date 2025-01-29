'''
Allows users to add tasks, view tasks, delete tasks and save tasks to  a file.
'''

tasks = []

def add_tasks(task):
    tasks.append(task)
    print(f"task added: {task}")

def view_tasks():
    if not tasks:
        print("No taks available.")
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

def main():
    while True:
        print("\nOptions: add | view | delete | exit")
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
        elif choice == "exit":
            print("Goodbye!")
            break
        else:
            print("Invalid command! Try again.")

if __name__ == "__main__":
    main()