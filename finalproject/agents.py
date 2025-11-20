from openai import OpenAI
from api_key import OPENAI_API_KEY
from notes import list_notes
from tasks import list_tasks

client = OpenAI(api_key=OPENAI_API_KEY)

def gpt(prompt):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content


def summarize_notes():
    notes = list_notes()
    if notes.startswith("No notes"):
        return "No notes to summarize."
    return gpt(f"Summarize these notes:\n{notes}")

def task_overview():
    tasks = list_tasks()
    if tasks.startswith("No tasks"):
        return "You have no tasks."
    return gpt(f"Give a helpful overview of these tasks:\n{tasks}")

def plan_task(task_title):
    return gpt(f"Break the task '{task_title}' into simple steps.")

def ask_ai(question):
    return gpt(question)