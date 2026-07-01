#!/usr/bin/env bash
set -euo pipefail

usage() {
  printf 'Usage: %s <branch-name>\n' "$0" >&2
}

if [ "$#" -ne 1 ]; then
  usage
  exit 64
fi

branch_name="$1"

if [ -z "$branch_name" ]; then
  usage
  exit 64
fi

git rev-parse --show-toplevel >/dev/null

if [ -n "$(git status --porcelain)" ]; then
  printf 'Refusing to switch branches with uncommitted changes:\n' >&2
  git status --short >&2
  exit 1
fi

if git show-ref --verify --quiet "refs/heads/$branch_name"; then
  printf 'Local branch already exists: %s\n' "$branch_name" >&2
  exit 1
fi

if git ls-remote --exit-code --heads origin "$branch_name" >/dev/null 2>&1; then
  printf 'Remote branch already exists: origin/%s\n' "$branch_name" >&2
  exit 1
fi

git switch main
git pull origin main
git switch -c "$branch_name"
