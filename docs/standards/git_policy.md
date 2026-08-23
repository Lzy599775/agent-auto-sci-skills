# Git Policy

## Branching

- Never develop directly on the default branch.
- Use descriptive branches such as `feature/`, `fix/`, `docs/`, `analysis/`, `methods/`, or `manuscript/`.
- Synchronize the base branch with fast-forward-only pulls.

## Before commit

1. Run `git status`.
2. Review `git diff`.
3. Stage intended paths explicitly.
4. Review `git diff --staged`.
5. Verify no secrets, private source material, unrelated files, or generated clutter are included.

## Commit and push

- Use specific messages such as `docs: add evidence standards`.
- Do not amend or rewrite shared history by default.
- Push only the task branch.
- Never force push.

## Pull requests

- Use Draft PRs for incomplete or validation-stage work.
- Include summary, files changed, validation, risks, and rollback/review notes.
- Do not merge automatically.
- Treat merge, branch deletion with unique work, and repository publication as explicit-approval actions.
