# API Configuration and Security

Use this file when configuring automated research workflows.

## 1. Do Not Store Secrets in Skills

Never place real API keys, tokens, OAuth strings, private database credentials, or reviewer-sensitive information in:

- `SKILL.md`
- `references/*.md`
- `agents/openai.yaml`
- evolution HTML or JSON
- public markdown reports
- git-tracked examples

Use local `.env` files, OS environment variables, or the user's approved secret manager.

## 2. AutoSci-Inspired Optional API Roles

| Variable | Role | Required locally? |
|---|---|---|
| `SEMANTIC_SCHOLAR_API_KEY` | Citation graph, citation counts, related-paper search | Optional; useful for large corpus work |
| `DEEPXIV_TOKEN` | Semantic paper search, TLDR, trending papers | Optional; only if the project uses DeepXiv |
| `LLM_API_KEY` | Independent reviewer LLM | Optional |
| `LLM_BASE_URL` | OpenAI-compatible endpoint for reviewer model | Optional |
| `LLM_MODEL` | Reviewer model name | Optional |
| `LLM_FALLBACK_MODEL` | Fallback model if primary reviewer fails | Optional |
| `ARXIV_CATEGORIES` | Daily paper monitoring categories | Optional |

For this project, the safest default is no external reviewer LLM unless the user explicitly configures it.

## 3. Recommended Local `.env` Template

```text
SEMANTIC_SCHOLAR_API_KEY=
DEEPXIV_TOKEN=
LLM_API_KEY=
LLM_BASE_URL=
LLM_MODEL=
LLM_FALLBACK_MODEL=
ARXIV_CATEGORIES=cs.LG,cs.CV,cs.CL,cs.AI,stat.ML
```

## 4. Configuration Workflow

1. Explain what each key enables and what works without it.
2. Ask the user to place keys in a local untracked `.env`.
3. Verify `.gitignore` excludes `.env`.
4. Test each API with a small non-sensitive query.
5. Record only the availability status, not the key value.

## 5. Research Data Safety

- Keep full-text PDFs and private reviewer materials local.
- HTML evolution archive should summarize skills and changes, not expose copyrighted text or raw data.
- When using third-party APIs, do not send unpublished sensitive findings unless the user explicitly approves.
- For journal submissions, separate public reproducibility material from private analysis notebooks.


