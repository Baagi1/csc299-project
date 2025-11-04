import json
import os

DATA_FILE = "data.json"

def load_data():
    if not os.path.exists(DATA_FILE):
        return {"tasks": [], "notes": []}
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

def add_task(description):
    data = load_data()
    task = {"id": len(data["tasks"]) + 1, "description": description}
    data["tasks"].append(task)
    save_data(data)
    print(f"✅ Task added: {description}")

def list_tasks():
    data = load_data()
    if not data["tasks"]:
        print("No tasks found.")
        return
    print("\n📌 Tasks:")
    for task in data["tasks"]:
        print(f"{task['id']}. {task['description']}")

def search_tasks(keyword):
    data = load_data()
    results = [t for t in data["tasks"] if keyword.lower() in t['description'].lower()]
    if not results:
        print("No tasks match.")
    else:
        for task in results:
            print(f"{task['id']}. {task['description']}")

def add_note(text):
    data = load_data()
    note = {"id": len(data["notes"]) + 1, "text": text}
    data["notes"].append(note)
    save_data(data)
    print("🧠 Note added.")

def list_notes():
    data = load_data()
    if not data["notes"]:
        print("No notes saved.")
        return
    print("\n🧾 Notes:")
    for note in data["notes"]:
        print(f"{note['id']}. {note['text']}")

def search_notes(keyword):
    data = load_data()
    results = [n for n in data["notes"] if keyword.lower() in n["text"].lower()]
    if not results:
        print("No notes found.")
    else:
        for note in results:
            print(f"{note['id']}. {note['text']}")

def main():
    print("Welcome to PKMS!")
    print("Commands: add_task, list_tasks, search_tasks, add_note, list_notes, search_notes, quit")

    while True:
        cmd = input("\nvibe> ").strip().lower()

        if cmd.startswith("add_task"):
            desc = cmd.replace("add_task", "").strip()
            if desc:
                add_task(desc)
            else:
                print("Type: add_task do homework")

        elif cmd == "list_tasks":
            list_tasks()

        elif cmd.startswith("search_tasks"):
            keyword = cmd.replace("search_tasks", "").strip()
            search_tasks(keyword)

        elif cmd.startswith("add_note"):
            text = cmd.replace("add_note", "").strip()
            add_note(text)

        elif cmd == "list_notes":
            list_notes()

        elif cmd.startswith("search_notes"):
            keyword = cmd.replace("search_notes", "").strip()
            search_notes(keyword)

        elif cmd == "quit":
            print("Goodbye! ✅")
            break

        else:
            print("Unknown command.")

if __name__ == "__main__":
    main()