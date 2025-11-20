# Task Manager CLI

Simple Python CLI to add/list/show/delete tasks persisted to a JSON file.

Usage (run from project root):

python -m task_manager_cli.cli add --title "Buy milk" --description "2L"
python -m task_manager_cli.cli list

By default tasks are stored under `~/.task_manager/tasks.json`. Override with `TASKS_PATH` env var or `--path` flag.

Testing

Create a virtualenv and install dev deps, then run pytest:

```bash
python3 -m venv .venv
.venv/bin/pip install -U pip pytest
PYTHONPATH=tools .venv/bin/pytest -q
```
