---
name: release
description: Validate and release the current feature branch in this repository by committing its intended changes, updating main, squash-merging the feature into one detailed release commit, and pushing main to trigger GitHub Pages. Use when the user says to release, ship, or publish completed site changes to production.
---

# Release

Release completed work from the current feature branch as one mainline commit. Invocation authorizes the final push to `origin/main`; do not open a pull request or require `gh`.

## Workflow

1. Inspect `git status -sb`, the diff, current branch, and remote tracking state.
   - Require a non-`main` feature branch.
   - If changes appear unrelated or the intended scope is unclear, stop and ask before staging.
   - Never discard or clean local changes.
2. Run `git diff --check` and the production validation:

   ```bash
   hugo --gc --minify --destination /tmp/rfive-release-build
   ```

3. Commit feature-branch changes when present.
   - Stage only the inspected files using explicit paths.
   - Use a concise subject and a body that explains the major design, content, and behavior changes.
   - If the worktree is already clean, release the branch commits as-is.
4. Update and stage the squash merge:

   ```bash
   git fetch origin
   git switch main
   git merge --ff-only origin/main
   git merge --squash <feature-branch>
   ```

5. Inspect the staged status and diff summary. Confirm they match the feature scope, then run:

   ```bash
   git diff --cached --check
   hugo --gc --minify --destination /tmp/rfive-main-release-build
   ```

6. Create one detailed release commit on `main`.
   - Use an imperative subject describing the overall release.
   - Add body paragraphs summarizing the important user-facing changes and implementation themes.
   - Do not reuse a vague message such as `Release changes`.
7. Push `main` to trigger the GitHub Pages workflow:

   ```bash
   git push origin main
   ```

8. Verify `git status -sb` and the latest commit. Report:
   - feature commit, when one was created;
   - squash release commit;
   - production build result;
   - push target and deployment trigger;
   - final worktree state.

## Safety

- Stop on build failures, merge conflicts, a dirty `main`, non-fast-forward updates, or unexpected staged files.
- Do not force-push, delete branches, reset commits, or bypass validation.
- Preserve the feature branch after release.
