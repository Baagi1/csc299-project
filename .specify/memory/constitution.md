# <!--
# Sync Impact Report
# Version change: unknown_old -> 1.0.0
# Modified principles:
# - PRINCIPLE_1_NAME (template) -> I. Library-First (added concrete rules)
# - PRINCIPLE_2_NAME (template) -> II. CLI & Text I/O (clarified I/O contract)
# - PRINCIPLE_3_NAME (template) -> III. Test-First (strengthened mandatory language)
# - PRINCIPLE_4_NAME (template) -> IV. Integration & Contract Testing (clarified requirements)
# - PRINCIPLE_5_NAME (template) -> V. Observability, Versioning, Simplicity (combined guidance)
# Added sections:
# - Additional Constraints (security & performance)
# - Development Workflow & Quality Gates
# Removed sections: none
# Templates updated:
# - .specify/templates/plan-template.md ✅ updated
# - .specify/templates/spec-template.md ✅ updated
# - .specify/templates/tasks-template.md ✅ updated
# Follow-up TODOs:
# - RATIFICATION_DATE left as TODO (file: .specify/memory/constitution.md)
# - Review other .specify templates and scripts for phrasing referencing old placeholder tokens
#
# -->

# Speckit Constitution
<!-- Project constitution generated from template and aligned with repository conventions -->

## Core Principles

### I. Library-First
Every feature MUST be designed as a discrete, importable library or module where practical. Libraries
are the primary unit of design and distribution: they MUST be self-contained, have clear public
APIs, include automated tests, and ship with documentation and an example/quickstart. Organizational-
only or monolithic modules that cannot be independently tested or reused are DISCOURAGED and
require explicit governance approval.

### II. CLI & Text I/O
All libraries and tools SHOULD expose a small, well-documented CLI surface when appropriate, and
adhere to text I/O conventions: use stdin/args for input, stdout for primary results, and stderr for
diagnostics and errors. Where machine interoperability is required, a stable JSON mode MUST be
provided alongside human-readable output.

### III. Test-First (NON-NEGOTIABLE)
Testing is mandatory. Before significant implementation, unit and contract tests MUST be written and
reviewed. The development cycle SHOULD follow Red-Green-Refactor: tests written to define behavior,
verified failing, implementation added, then refactored. Pull requests MUST include tests that cover
new behavior and maintain or improve existing coverage.

### IV. Integration & Contract Testing
Integration tests and contract tests are required for changes that affect public interfaces, inter-
service communication, or shared schemas. Integration tests MUST exercise end-to-end flows where
reasonable, and contract tests MUST be used to detect breaking changes early.

### V. Observability, Versioning, Simplicity
Projects MUST provide structured logging or event traces for key operations, and sensible defaults
for observability. Versioning MUST follow semantic versioning for public packages and APIs
(MAJOR.MINOR.PATCH). Designs MUST favour simplicity (YAGNI) and explicit trade-offs must be
documented when complexity is introduced.

## Additional Constraints

Security: All code handling secrets, credentials, or PII MUST follow established secure coding
practices and be audited prior to production deployment. Sensitive configuration MUST live in
environment-specific configuration stores (not committed to VCS).

Performance: Services and libraries should document performance goals in their spec. Any change that
could impact p95/p99 latency or throughput MUST include a performance assessment in the plan.

## Development Workflow & Quality Gates

Code reviews are mandatory for all changes to main branches. Every PR MUST include a plan for
testing (unit, integration, contract), a changelog entry for public APIs, and a short migration note
if applicable. CI pipelines MUST run unit tests, linters, and security scans. Breaking changes to
public APIs MUST include a migration guide and a deprecation window.

## Governance
<!-- Constitution supersedes informal practices; amendments follow the procedure below -->

Amendments to this constitution MUST be proposed via pull request that includes: the exact text
changes, a concise rationale, an impact assessment for templates and enforcement points, and at
least two maintainer approvals. Principle removals or redefinitions that change governance or
enforcement semantics are considered MAJOR changes and require a MAJOR version bump and broad
notification to stakeholders.

All PRs that touch project conventions MUST reference this constitution and include a short
compliance checklist demonstrating how changes align with the principles above.

**Version**: 1.0.0 | **Ratified**: 2025-11-18 | **Last Amended**: 2025-11-18
