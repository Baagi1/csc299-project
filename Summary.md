CSC 299 Final Project Summary

For my CSC 299 final project, I built a complete system that combines a personal knowledge manager, a task manager, a terminal chat interface, and optional AI tools. This project is the final result of everything I learned over the whole quarter, building from the earlier tasks and expanding them into a full application.

The system includes:

a Personal Knowledge Management System (PKMS) for storing and searching notes

a Task Manager with priority, due dates, and status

a terminal-based chat interface that lets me interact with all parts of the system

AI agents that can give suggestions or answer questions
Everything runs in Python and saves data in JSON so it works on macOS, Windows, and Linux without needing extra setup.

This summary explains how I planned and built the project, the tools I used, what worked well, and what challenges I faced along the way.

1. Planning the Project

At the start, I wasn’t completely sure how all the requirements fit together. I had never really used tools like Git, GitHub, VS Code, virtual environments, or JSON storage before this class. I also didn’t fully understand how a PKMS works or how a terminal chatbot should behave.

So I used ChatGPT to break everything down for me. I asked questions like:

What functions should a PKMS include?

How should tasks and notes be saved in JSON?

What should the command-line interface look like?

How do I connect AI without forcing the user to provide an API key?

What’s the best way to structure the project?

After a lot of planning, I created a clear folder layout with modules for tasks, notes, storage, agents, and the CLI. Having this blueprint made everything easier once I started coding.

2. How Tasks 1–5 Helped Me Build the Final Project

Even though the final project is separate from Tasks 1–5, those prototypes taught me everything I needed.

Task 1 – Basic JSON workflow

Task 1 taught me the core idea I reused almost everywhere:
read JSON → edit Python dictionary → write JSON back.

This became the foundation of the storage system in my final project.

Task 2 – Multiple modules

Task 2 introduced using multiple files, filtering logic, and a more organized project structure.
This heavily influenced how I designed the task manager and storage modules.

Task 3 – Testing

Task 3 was about pytest and taught me:

how to write basic tests

how testing reveals problems early

how to check JSON structure

why clean architecture matters

When building the final project, I repeatedly tested each new function the moment I wrote it.

Task 4 – AI Integration

This task taught me the most. I learned how to:

call the OpenAI API

write prompts

handle missing API keys

create fallback behavior

deal with token errors

This prototype directly shaped my AI agent module in the final project.

Task 5 – Specifications

Task 5 taught me how to plan before coding:

writing specifications

defining behaviors

describing module responsibilities
This helped me design my final project more clearly.

3. Using AI Tools While Building the Project

I used GPT-5.1 the most throughout the project. I used it for:

planning the architecture

writing the first versions of modules

debugging errors

designing CLI commands

explaining Python concepts

I also used:

Claude Code for early drafts

GitHub Copilot for autocomplete and small code suggestions

Copilot helped speed up writing loops, conditions, and repetitive code, but it wasn’t always correct, so I still had to carefully check everything.

For the AI features in the final project, I used OpenAI’s gpt-4.1-mini, but I also included a mode that works without an API key so the system is usable by anyone.

4. Testing the Final System

I constantly tested during development by running commands like:

tasks add

tasks list

notes add

notes search

chat tasks

chat notes

I checked:

whether JSON saved correctly

whether filters worked

whether the AI agent behaved correctly

whether the chat interface responded naturally
This helped me catch bugs early and keep everything consistent.

5. What Worked Well
AI-Assisted Planning

Using ChatGPT, Copilot, and Claude for design and planning made everything much easier.
AI helped me structure the project, design functions, and understand errors.

Modular Design

Separating everything into different modules (tasks, notes, storage, agents) made the project cleaner and easier to debug.

Optional AI Mode

Having AI as optional was a great decision:

if no API key → offline mode

if API key exists → enhanced AI mode
This makes the system easier for anyone to run.

6. Challenges I Faced
GitHub Merge Conflicts

I ran into a lot of merge conflicts while pushing updates.
Sometimes the README mixed with older files, or Git blocked a push because branches didn’t match.
This forced me to learn how to resolve conflicts and understand Git better.

Overcomplicating AI at First

My first attempt at the AI agent module was way too complex.
I tried adding things like embeddings, chains of prompts, and multiple sub-agents.
It didn’t work at all, so I deleted it and started over with a simpler, functional design.

Virtual Environment Issues

I struggled with:

imports breaking

forgetting to activate the venv

folder names causing problems

missing __init__.py files

Fixing these made my whole project run smoothly.

Conclusion

Overall, this final project taught me more than I expected. I learned how to plan software, how to work with multiple modules, how to use JSON for storage, how to test correctly, and how to integrate AI. I also learned a lot about debugging, Git, virtual environments, and how powerful AI coding assistants can be when used properly.

This project was challenging but also one of the most useful learning experiences I’ve had, and I feel more confident now in building real software.
