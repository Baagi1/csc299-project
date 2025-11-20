from tasks import add_task, list_tasks, complete_task, delete_task
from notes import add_note, list_notes, view_note
from agents import summarize_notes, task_overview, plan_task, ask_ai

def show_help():
    return """
Commands:
  help                         Show commands
  exit                         Quit

Tasks:
  add task <title>             Add a task
  list tasks                   Show tasks
  complete task <num>          Complete a task
  delete task <num>            Delete a task

Notes:
  add note                     Add a note
  list notes                   Show notes
  view note <num>              View a note

AI (OpenAI):
  summarize notes              GPT summary
  task overview                GPT task analysis
  plan task <title>            Break a task into steps
  ask ai <question>            Ask GPT anything
"""

def chat():
    print("=== CSC299 Final Project Chat Interface ===")
    print("Type 'help' for commands.\n")

    while True:
        msg = input("You: ").strip()

        if msg == "exit":
            print("Goodbye!")
            break

        elif msg == "help":
            print(show_help())

        elif msg.startswith("add task"):
            title = msg.replace("add task", "").strip()
            print(add_task(title))

        elif msg == "list tasks":
            print(list_tasks())

        elif msg.startswith("complete task"):
            num = int(msg.split()[-1])
            print(complete_task(num))

        elif msg.startswith("delete task"):
            num = int(msg.split()[-1])
            print(delete_task(num))

        elif msg == "list notes":
            print(list_notes())

        elif msg == "add note":
            title = input("Title: ")
            content = input("Content: ")
            print(add_note(title, content))

        elif msg.startswith("view note"):
            num = int(msg.split()[-1])
            print(view_note(num))

        elif msg == "summarize notes":
            print(summarize_notes())

        elif msg == "task overview":
            print(task_overview())

        elif msg.startswith("plan task"):
            title = msg.replace("plan task", "").strip()
            print(plan_task(title))

        elif msg.startswith("ask ai"):
            question = msg.replace("ask ai", "").strip()
            print(ask_ai(question))

        else:
            print("Unknown command. Type 'help'.")
            

if __name__ == "__main__":
    chat()