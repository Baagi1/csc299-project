from storage import load_json, save_json

NOTES_FILE = "notes.json"

def list_notes():
    notes = load_json(NOTES_FILE)
    if not notes:
        return "No notes found."
    output = ""
    for idx, n in enumerate(notes, 1):
        output += f"{idx}. {n['title']}\n"
    return output

def add_note(title, content):
    notes = load_json(NOTES_FILE)
    notes.append({
        "title": title,
        "content": content
    })
    save_json(NOTES_FILE, notes)
    return "Note added."

def view_note(number):
    notes = load_json(NOTES_FILE)
    if number < 1 or number > len(notes):
        return "Invalid note number."
    note = notes[number - 1]
    return f"Title: {note['title']}\n\n{note['content']}"