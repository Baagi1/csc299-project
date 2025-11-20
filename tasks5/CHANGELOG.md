# Changelog

All notable changes to this project will be documented in this file.

## Unreleased (001-task-manager-cli) - 2025-11-18

### Added
- Implemented a simple Python CLI Task Manager (`tools/task_manager_cli`) with commands:
  - `add` — add a task with title and optional description
  - `list` — show a brief list of tasks
  - `show` — display a task's full title and description
  - `delete` — remove a task by id
- Local JSON persistence (default: `~/.task_manager/tasks.json`) with atomic writes.
- Unit and integration tests added (`tests/test_storage.py`, `tests/test_cli_end_to_end.py`).
- Basic documentation: `tools/task_manager_cli/README.md`, `CONTRIBUTING.md`.
- CI workflow: `.github/workflows/test-task-manager-cli.yml` runs tests on push/PR.
- Observability: lightweight logging added to CLI and storage for key operations.

### Notes
- This change follows the project's Speckit constitution: library-first design, test-first development, and CI-driven validation.
