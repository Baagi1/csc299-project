from storage import load_json, save_json

TASK_FILE = "tasks.json"

def list_tasks():
    tasks = load_json(TASK_FILE)
    if not tasks:
        return "No tasks found."
    output = ""
    for idx, t in enumerate(tasks, 1):
        output += f"{idx}. {t['title']} - {'Done' if t['done'] else 'Not Done'}\n"
    return output

def add_task(title):
    tasks = load_json(TASK_FILE)
    tasks.append({"title": title, "done": False})
    save_json(TASK_FILE, tasks)
    return "Task added."

def complete_task(number):
    tasks = load_json(TASK_FILE)
    if number < 1 or number > len(tasks):
        return "Invalid task number."
    tasks[number - 1]["done"] = True
    save_json(TASK_FILE, tasks)
    return "Task marked complete."

def delete_task(number):
    tasks = load_json(TASK_FILE)
    if number < 1 or number > len(tasks):
        return "Invalid task number."
    tasks.pop(number - 1)
    save_json(TASK_FILE, tasks)
    return "Task deleted."