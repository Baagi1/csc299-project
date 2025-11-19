````markdown
# Tasks: Simple Python CLI Task Manager

**Input**: Design from `specs/001-task-manager-cli/spec.md`
**Prerequisites**: plan.md (optional), spec.md (required)

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [X] T001 Create feature directory `tools/task_manager_cli/`
- [X] T002 [P] Create Python packaging files: `tools/task_manager_cli/pyproject.toml` and `.gitignore`
- [X] T003 [P] Create README with usage examples: `tools/task_manager_cli/README.md`
- [X] T004 [P] Add project-level `tests/` directory and initial test runner config: `pytest.ini`

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core modules that MUST be in place before implementing CLI commands

- [X] T005 Implement Task model dataclass in `tools/task_manager_cli/models.py`
- [X] T006 Implement JSON storage module (read/write/atomic) in `tools/task_manager_cli/storage.py`
- [X] T007 Implement configuration helper supporting default path and override via env/flag in `tools/task_manager_cli/config.py`
- [X] T008 [P] Add helper for file locking or atomic write in `tools/task_manager_cli/atomic.py`

**Checkpoint**: Foundation ready - CLI command work can begin

---

## Phase 3: User Story 1 - Manage tasks (Priority: P1) 🎯 MVP

**Goal**: Provide add, list, show, and delete operations for tasks persisted in a local JSON file

**Independent Test**: End-to-end test using a temporary JSON file that runs `task add`, `task list`, `task show <id>`, and `task delete <id>` and asserts expected outputs and file contents.

### Implementation Tasks

- [X] T009 [P] [US1] Create CLI entry module `tools/task_manager_cli/cli.py` (argparse-based)
- [X] T010 [US1] Implement `add` command in `tools/task_manager_cli/cli.py` (persists via `storage.py`)
- [X] T011 [US1] Implement `list` command in `tools/task_manager_cli/cli.py` (reads from `storage.py`)
- [X] T012 [US1] Implement `show` command in `tools/task_manager_cli/cli.py` (shows full title & description)
- [X] T013 [US1] Implement `delete` command in `tools/task_manager_cli/cli.py` (removes by id)
- [X] T014 [US1] Add `__main__` entrypoint to `tools/task_manager_cli/__main__.py` to allow `python -m task_manager_cli`
- [ ] T015 [US1] Add CLI executable wrapper script at `bin/task` (or a small README instruction to run via `python -m`)

### Tests (recommended – supports the constitution's Test-First guidance)

- [X] T016 [P] [US1] Create unit tests for storage and model in `tests/test_storage.py`
- [X] T017 [P] [US1] Create end-to-end CLI integration tests in `tests/test_cli_end_to_end.py` using a temp JSON path

**Checkpoint**: User Story 1 should be fully functional and testable independently

---

## Phase 4: Polish & Cross-Cutting Concerns

**Purpose**: Documentation, packaging, CI, and cross-cutting improvements

- [ ] T018 Update `tools/task_manager_cli/README.md` with installation and examples (include default JSON path and env var override)
- [ ] T019 [P] Add basic CI workflow for tests: `.github/workflows/test-task-manager-cli.yml`
- [ ] T020 [P] Add license and contribution guidelines: `tools/task_manager_cli/CONTRIBUTING.md`
- [ ] T021 [P] Ensure logging/observability for key operations in `storage.py` and `cli.py` (structured print or logging)

---

## Dependencies & Execution Order

1. Foundation (Phase 2: T005–T008) MUST complete before User Story implementation (Phase 3: T009–T015).
2. Within User Story 1, tests (T016–T017) can be written in parallel with implementation tasks but should
   be runnable once storage and models are present.

## Parallel Opportunities

- Tasks marked with `[P]` can be executed in parallel (independent files): T002, T003, T004, T008, T009 (partial), T016, T017, T019, T020, T021.

## Implementation Strategy

### MVP First

1. Complete Phase 1 + Phase 2 foundational tasks: T001–T008.
2. Implement minimal CLI with `add` and `list` (T009, T010, T011) and a basic storage module (T006).
3. Run end-to-end manual test demonstrating add/list using a temporary JSON file.
4. Implement `show` and `delete` (T012, T013) and add integration tests (T017).
5. Polish docs and CI (Phase 4 tasks).

## Task counts & summary

- Total tasks: 21
- Tasks by story:
  - Setup/Foundation/Polish: 14
  - User Story 1 (US1): 7 (T009–T015 plus tests T016–T017 grouped)

## Format validation

All tasks follow the required checklist format: `- [ ] T### [P?] [US#] Description with file path`.

## Try it (examples)

Parallel example (run setup tasks in parallel):

```bash
# Create files  (can be run in parallel where marked [P])
mkdir -p tools/task_manager_cli && mkdir -p tests
touch tools/task_manager_cli/__init__.py tools/task_manager_cli/cli.py tools/task_manager_cli/storage.py
touch tools/task_manager_cli/models.py tools/task_manager_cli/config.py
```

End of tasks.md
````
