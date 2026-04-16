---
description: Automatically format Python code with ruff on pull requests
on:
  pull_request:
    types: [opened, synchronize]
  workflow_dispatch:
permissions: read-all
steps:
  - uses: actions/checkout@v4
    with:
      persist-credentials: false
  - uses: actions/setup-python@v5
    with:
      python-version: "3.12"
  - name: Install dev tools
    run: |
      python -m pip install --upgrade pip
      python -m pip install ruff
  - name: Ruff format check
    run: ruff format --check .
  - name: Ruff lint
    run: ruff check .
tools:
  bash:
    - "git:*"
  edit:
safe-outputs:
  add-comment:
  create-pull-request:
  missing-tool:
    create-issue: true
timeout-minutes: 10
---

# Python Format Check

You are an AI agent that reviews the results of ruff checks that already ran as normal CI steps.

## Your Task

1. **Review the CI step outputs** from the preceding runner steps:
   - `ruff format --check .` — formatting check
   - `ruff check .` — linting check

2. **If ruff found formatting issues**, run `ruff format .` and `ruff check . --fix` to auto-fix them, then use `git status` and `git diff` to see what changed.

3. **If fixes were made**:
   - Use the `create-pull-request` safe output to create a commit with the formatting fixes
   - Title: "🤖 Auto-format: Fix Python formatting and linting"
   - Body: Include a summary of what was fixed (files changed, types of fixes)

4. **Add a comment** with:
   - ✅ Summary of formatting/linting fixes applied (if any)
   -  Overall status (all checks passed, or issues found)

## Guidelines

- Be concise but informative in your comment
- Use emojis and formatting for readability
- If there are no issues, keep the comment short and positive
- If fixes were made, explain what was changed
- For type errors, provide clear actionable feedback
