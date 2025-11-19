import tempfile
import os
from task_manager_cli.storage import read_tasks, write_tasks, next_id
from task_manager_cli.models import Task


def test_storage_read_write(tmp_path):
    p = tmp_path / "tasks.json"
    tasks = [Task(id=1, title="t1", description="d1")]
    write_tasks(str(p), tasks)
    loaded = read_tasks(str(p))
    assert len(loaded) == 1
    assert loaded[0].title == "t1"


def test_next_id_empty():
    assert next_id([]) == 1


def test_next_id_nonempty():
    tasks = [Task(id=1, title="a"), Task(id=2, title="b")]
    assert next_id(tasks) == 3
