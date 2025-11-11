# __main__.py
import os
from openai import OpenAI
from dotenv import load_dotenv

# Load .env if present
load_dotenv()

API_KEY = os.getenv("OPENAI_API_KEY")
if not API_KEY:
    raise RuntimeError(
        "OPENAI_API_KEY not found. Set it with:\n"
        "export OPENAI_API_KEY='sk-xxx'  (or create a .env file with OPENAI_API_KEY)"
    )

client = OpenAI(api_key=API_KEY)

# Two sample paragraph-length task descriptions
task_descriptions = [
    "I need to finish my math homework before Friday. It includes solving 20 algebra problems about linear equations and inequalities. I also have to complete a short quiz online, which is worth 10% of my grade.",
    "I want to organize all the files on my computer because it’s messy. I plan to create folders for school, personal stuff, and downloads, and sort everything so I can find things more easily later."
]

def summarize_task(description: str) -> str:
    """Send description to Chat Completions and return a short phrase summary."""
    response = client.chat.completions.create(
        model="gpt-5-mini",
        messages=[
            {"role": "system", "content": "Summarize the task into a short phrase."},
            {"role": "user", "content": description}
        ],
        max_tokens=20,
        temperature=0.0,
    )
    # safe access of response
    try:
        return response.choices[0].message.content.strip()
    except Exception:
        return "<no summary returned>"

def main():
    for i, desc in enumerate(task_descriptions, start=1):
        print(f"\nTask {i} description:\n{desc}\n")
        summary = summarize_task(desc)
        print("Summary:", summary)

if __name__ == "__main__":
    main()