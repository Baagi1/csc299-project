import json
import os
import logging
from typing import List
from .models import Task
from .atomic import atomic_write

logger = logging.getLogger(__name__)


def read_tasks(path: str) -> List[Task]:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    if not os.path.exists(path):
        return []
    with open(path, "r", encoding="utf-8") as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            return []
    tasks = [Task(**item) for item in data]
    logger.debug("read %d tasks from %s", len(tasks), path)
    return tasks


def write_tasks(path: str, tasks: List[Task]):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    data = [t.to_dict() for t in tasks]
    atomic_write(path, json.dumps(data, ensure_ascii=False, indent=2))
    logger.info("wrote %d tasks to %s", len(tasks), path)


def next_id(tasks: List[Task]) -> int:
    if not tasks:
        return 1
    return max(t.id for t in tasks) + 1
