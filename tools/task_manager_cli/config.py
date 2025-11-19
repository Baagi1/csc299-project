import os


def default_tasks_path():
    return os.path.expanduser(os.environ.get("TASKS_PATH", "~/.task_manager/tasks.json"))
