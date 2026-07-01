---
name: start-feature-branch
description: Use when starting work on a new feature in this repository and the user provides a feature branch name. Checks for a clean worktree, switches to main, pulls from origin, then creates and switches to a new local branch named after the feature.
---

# Start Feature Branch

Use this skill whenever the user asks to start a new feature, create a new feature branch, or begin work from a fresh `main` branch in this repository.

## Workflow

1. Require a branch name from the user. Use the provided feature name exactly when it is already a valid git branch name. If the name is prose, normalize it to lowercase hyphen-case.
2. Check the worktree with `git status --short --branch`.
3. If there are uncommitted changes, stop and ask before switching branches.
4. Run the bundled script from the repository root:

   ```bash
   .codex/skills/start-feature-branch/scripts/start-feature-branch.sh <branch-name>
   ```

5. Report the final branch and whether `main` was updated.

## Behavior

The script performs this sequence:

```bash
git switch main
git pull origin main
git switch -c <branch-name>
```

It fails early if:

- It is not run inside a git repository.
- The branch name is missing.
- The worktree has uncommitted changes.
- The target branch already exists locally or on `origin`.

Do not use destructive cleanup commands to make the worktree clean. Ask the user how to handle any local changes instead.
