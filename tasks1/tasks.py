import json
import os
import sys

DATA_FILE = "tasks_data.json"

def load_tasks():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_tasks(tasks):
    with open(DATA_FILE, "w") as f:
        json.dump(tasks, f, indent=4)

def add_task(description):
    tasks = load_tasks()
    task = {"id": len(tasks) + 1, "description": description}
    tasks.append(task)
    save_tasks(tasks)
    print(f"✅ Task added: {description}")

def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
        return
    for task in tasks:
        print(f"{task['id']}. {task['description']}")

def search_tasks(keyword):
    tasks = load_tasks()
    results = [t for t in tasks if keyword.lower() in t['description'].lower()]
    if not results:
        print(f"No tasks found matching '{keyword}'.")
    else:
        for task in results:
            print(f"{task['id']}. {task['description']}")

def show_help():
    print("""
Usage:
    python3 tasks.py add "task description"   → Add a new task
    python3 tasks.py list                     → List all tasks
    python3 tasks.py search "keyword"         → Search tasks
    python3 tasks.py help                     → Show this help
""")

def main():
    if len(sys.argv) < 2:
        show_help()
        return

    command = sys.argv[1].lower()

    if command == "add" and len(sys.argv) > 2:
        description = " ".join(sys.argv[2:])
        add_task(description)
    elif command == "list":
        list_tasks()
    elif command == "search" and len(sys.argv) > 2:
        keyword = " ".join(sys.argv[2:])
        search_tasks(keyword)
    else:
        show_help()

if __name__ == "__main__":
    main()