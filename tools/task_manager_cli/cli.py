import argparse
import sys
from .storage import read_tasks, write_tasks, next_id
from .models import Task
from .config import default_tasks_path


def parse_args(argv=None):
    parser = argparse.ArgumentParser(prog="task")
    sub = parser.add_subparsers(dest="cmd")

    add = sub.add_parser("add")
    add.add_argument("--title", required=True)
    add.add_argument("--description", default="")
    add.add_argument("--path", default=None)

    listp = sub.add_parser("list")
    listp.add_argument("--path", default=None)

    show = sub.add_parser("show")
    show.add_argument("id", type=int)
    show.add_argument("--path", default=None)

    delete = sub.add_parser("delete")
    delete.add_argument("id", type=int)
    delete.add_argument("--path", default=None)

    return parser.parse_args(argv)


def main(argv=None):
    args = parse_args(argv)
    path = args.path or default_tasks_path()

    if args.cmd == "add":
        if not args.title.strip():
            print("ERROR: title required", file=sys.stderr)
            return 2
        tasks = read_tasks(path)
        tid = next_id(tasks)
        task = Task(id=tid, title=args.title.strip(), description=args.description)
        tasks.append(task)
        write_tasks(path, tasks)
        print(f"Added task {task.id}: {task.title}")
        return 0

    if args.cmd == "list":
        tasks = read_tasks(path)
        for t in tasks:
            desc = (t.description[:50] + "...") if len(t.description) > 50 else t.description
            print(f"{t.id}: {t.title} - {desc}")
        return 0

    if args.cmd == "show":
        tasks = read_tasks(path)
        for t in tasks:
            if t.id == args.id:
                print(f"{t.id}: {t.title}\n{t.description}")
                return 0
        print("ERROR: task not found", file=sys.stderr)
        return 3

    if args.cmd == "delete":
        tasks = read_tasks(path)
        new = [t for t in tasks if t.id != args.id]
        if len(new) == len(tasks):
            print("ERROR: task not found", file=sys.stderr)
            return 3
        write_tasks(path, new)
        print(f"Deleted task {args.id}")
        return 0

    print("No command specified", file=sys.stderr)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
