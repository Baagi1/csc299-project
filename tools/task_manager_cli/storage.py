import json
import os
from typing import List
from .models import Task
from .atomic import atomic_write


def read_tasks(path: str) -> List[Task]:
    if not os.path.exists(path):
        return []
    with open(path, "r", encoding="utf-8") as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            return []
    return [Task(**item) for item in data]


def write_tasks(path: str, tasks: List[Task]):
    data = [t.to_dict() for t in tasks]
    atomic_write(path, json.dumps(data, ensure_ascii=False, indent=2))


def next_id(tasks: List[Task]) -> int:
    if not tasks:
        return 1
    return max(t.id for t in tasks) + 1
