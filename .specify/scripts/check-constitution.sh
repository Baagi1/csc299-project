#!/usr/bin/env bash
# Simple constitution consistency checker
# Usage: ./check-constitution.sh

set -euo pipefail

CONSTITUTION=".specify/memory/constitution.md"

if [[ ! -f "$CONSTITUTION" ]]; then
  echo "Constitution file not found: $CONSTITUTION" >&2
  exit 2
fi

errors=0

echo "Checking $CONSTITUTION"

# 1) No unresolved bracket tokens like [SOMETHING]
if grep -qE "\[[A-Z0-9_]+\]" "$CONSTITUTION"; then
  echo "ERROR: Found unresolved [PLACEHOLDER] tokens in $CONSTITUTION" >&2
  grep -nE "\[[A-Z0-9_]+\]" "$CONSTITUTION" || true
  errors=$((errors+1))
fi

# 2) Version looks like semver (allow bold or plain)
if ! grep -qE "Version\*?\*?:? [0-9]+\.[0-9]+\.[0-9]+" "$CONSTITUTION"; then
  echo "ERROR: Version line missing or not semver (MAJOR.MINOR.PATCH)" >&2
  errors=$((errors+1))
fi

# 3) Last Amended is ISO YYYY-MM-DD (allow bold or plain, flexible punctuation)
if ! grep -qE "Last Amended\*?\*?:? [0-9]{4}-[0-9]{2}-[0-9]{2}" "$CONSTITUTION"; then
  echo "ERROR: Last Amended date missing or not ISO YYYY-MM-DD" >&2
  errors=$((errors+1))
fi

# 4) Warn if RATIFICATION_DATE left TODO
if grep -q "TODO(RATIFICATION_DATE)" "$CONSTITUTION"; then
  echo "WARN: RATIFICATION_DATE left as TODO in constitution. Please fill if known." >&2
fi

if [[ $errors -gt 0 ]]; then
  echo "Validation failed: $errors error(s)" >&2
  exit 3
fi

echo "Constitution checks passed (notes may include WARNings)."
exit 0
