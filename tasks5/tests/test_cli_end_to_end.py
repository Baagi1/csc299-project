import subprocess
import sys
import tempfile
import json


def run_cmd(args, env=None):
    cmd = [sys.executable, "-m", "task_manager_cli.cli"] + args
    res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, env=env, text=True)
    return res


def test_cli_add_list_show_delete(tmp_path):
    p = tmp_path / "tasks.json"
    env = dict(**{**dict(os.environ), "TASKS_PATH": str(p)}) if False else None
    # add
    res = run_cmd(["add", "--title", "Buy milk", "--description", "2L", "--path", str(p)])
    assert res.returncode == 0
    # list
    res = run_cmd(["list", "--path", str(p)])
    assert "Buy milk" in res.stdout
    # show
    res = run_cmd(["show", "1", "--path", str(p)])
    assert "Buy milk" in res.stdout
    # delete
    res = run_cmd(["delete", "1", "--path", str(p)])
    assert res.returncode == 0
    # list should be empty
    res = run_cmd(["list", "--path", str(p)])
    assert res.stdout.strip() == ""
