import datetime
import os
import json

TASKS_FILE = "tasks.txt"

task_by_category = {
    "Work": [],
    "Personal": [],
    "Shopping": []
}

'''
def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            return [line.strip() for line in file.readlines()]
    return []
'''

def load_tasks():
    if os.path.exists(TASKS_FILE):
        try:
            with open(TASKS_FILE, "r") as file:
                data = json.load(file)

                for category, tasks in data.items():
                    for task in tasks:
                        if task["due_date"]:
                            task["due_date"] = datetime.datetime.strptime(task["due_date"], "%Y-%m-%d"),
                return data
        except(json.JSONDecodeError, KeyError):
            print("Error loading tasks. Starting with a new task list")

    return{
        "Work": [],
        "Personal": [],
        "Shopping": []
    }
'''
def save_tasks():
    with open(TASKS_FILE, "w") as file:
        for task in tasks:
            file.write(f"{task}\n")
    print("Tasks saved to file.")
'''
def save_tasks():
    with open(TASKS_FILE, "w") as file:
        json.dump(task_by_category, file, default= str)
    print("Tasks saved to file")

'''
def add_tasks(task):
    tasks.append(task)
    print(f"task added: {task}")
    save_tasks()
'''

def add_tasks(category, task, priority = "Medium", due_date = None):
    due_date = datetime.datetime.strptime(due_date, "%Y/%m/%d") if due_date else None
    task_by_category[category].append({"task": task, "priority": priority, "due_date": due_date, "completed": False})
    print(f"Task added: {task}, Category: {category}, Priority: {priority}, Due on: {due_date}")
    save_tasks()

'''
def view_tasks():
    if not tasks:
        print("No tasks available.")
    else:
        print("\nTo-Do List")
        for index, task in enumerate(tasks,start=1):
            print(f"{index}.{task}")
'''
def view_tasks(category):
    for index, task in enumerate(task_by_category[category], start=1):
        completed = "[X]" if task["completed"] else "[ ]"
        due = task["due_date"].strftime('%Y/%m/%d') if task["due_date"] else "No due date"
        print(f"Completed: {index}.{completed} | task: {task['task']} (Priority: {task['priority']}, Due: {due})")

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
            category = input("Enter category(Work, Personal, Shopping): ")
            task = input("Enter task: ").strip()
            priority = input("Enter Priority(High/Medium/Low): ").strip()
            due_date = input("Enter due date (YYYY/MM/DD) or leave blank: ").strip()
            add_tasks(category,task, priority, due_date)
        elif choice == "view":
            category = input("Enter category to view(Work, Personal, Shopping): ")
            view_tasks(category)
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