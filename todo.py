import json
import os

TASKS_FILE = 'tasks.txt'

def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks, file)

def add_task(tasks, task):
    tasks.append({'task': task, 'completed': False})
    save_tasks(tasks)

def view_tasks(tasks):
    for index, task in enumerate(tasks):
        status = '✓' if task['completed'] else '✗'
        print(f"{index + 1}. [{status}] {task['task']}")

def complete_task(tasks, index):
    if 0 <= index < len(tasks):
        tasks[index]['completed'] = True
        save_tasks(tasks)

def delete_task(tasks, index):
    if 0 <= index < len(tasks):
        tasks.pop(index)
        save_tasks(tasks)

def main():
    tasks = load_tasks()
    
    while True:
        print("\nTo-Do List:")
        view_tasks(tasks)
        print("\nOptions: add, complete, delete, quit")
        command = input("What would you like to do? ").strip().lower()

        if command == 'add':
            task = input("Enter a task: ")
            add_task(tasks, task)
        elif command == 'complete':
            index = int(input("Enter task number to complete: ")) - 1
            complete_task(tasks, index)
        elif command == 'delete':
            index = int(input("Enter task number to delete: ")) - 1
            delete_task(tasks, index)
        elif command == 'quit':
            break
        else:
            print("Unknown command.")

if __name__ == "__main__":
    main()
