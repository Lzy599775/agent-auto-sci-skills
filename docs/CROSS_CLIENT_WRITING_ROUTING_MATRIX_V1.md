# Cross-Client Writing Routing Matrix V1

This matrix is the parity contract for ChatGPT Web and Codex. The clients may use different retrieval and file tools, but they must preserve the same scientific contract, exemplar selection logic, read-scope claims, and anti-copying boundary.

Canonical public protocol: [`skills/agent-auto-sci-scicomm/references/academic_writing_exemplar_protocol.md`](../skills/agent-auto-sci-scicomm/references/academic_writing_exemplar_protocol.md)
Private preference profile: `Lzy599775/research-project-state-hub/shared/writing/ACADEMIC_WRITING_PROFILE_V1.md`

## Parity case

**Task:** “根据目标期刊近邻论文，修改 Discussion 的论证结构” / “Using near-neighbor papers from the target journal, revise the Discussion argument structure.”

| Contract step | Codex expected route | ChatGPT Web expected route | Required invariant |
|---|---|---|---|
| 1. Load preferences | `auto-sci-research` reads the shared profile when available | Project router loads `ACADEMIC_WRITING_PROFILE_V1` | Profile is a cross-project preference, not project scientific state. |
| 2. Select owner | `agent-auto-sci-scicomm`, plus a domain writing helper when applicable | Project writing router with the same communication owner | Domain owner may add evidence context but cannot become the polishing owner. |
| 3. Select mode | Explicit target-journal adaptation => `REQUIRED` | Same => `REQUIRED` | Explicit user intent wins over automatic classification. |
| 4. Build our maps | `OUR_EVIDENCE_MAP -> OUR_ARGUMENT_OUTLINE` | Same sequence in the Web response/workspace | No draft begins from exemplar prose. |
| 5. Retrieve exemplars | Zotero/verified corpus/current web retrieval; 3–5 per substantive section | Project-approved sources/current web retrieval; 3–5 per substantive section | Rank by function and scientific proximity; prestige/IF is supporting evidence only. |
| 6. Record scope | `FULLTEXT`, `ABSTRACT_ONLY`, or `METADATA_ONLY` in the story map | Same labels and claim limits | Only `FULLTEXT` permits full-manuscript structure claims. |
| 7. Compare functions | Discussion Move Map and Claim Ladder | Same maps, rendered in the Web workspace | Learn order and function, not wording, citations, claims, or causality. |
| 8. Draft | Draft from our evidence and argument outline | Same | Preserve design, effect direction, uncertainty, null/conflicting evidence, and measurement/scope limits. |
| 9. Style QC | Academic Prose Style Guard | Same canonical guard rules | Positive-first prose must not erase necessary boundaries. |
| 10. Polish/lint | `scipilot-writing-skill` | Web writing/style tools or the project’s equivalent | Final owner may improve expression but may not add facts or references. |

## Shared decision table

| User task | Mode | Exemplar search | Prose guard | Anti-copying check |
|---|---:|---:|---:|---:|
| “润色一句话” | `SKIP` | No | Existing prose route only | Not required |
| “重写 Introduction，目标 LUP” | `AUTO` when a verified exemplar is obtainable | Yes, per section | Yes | Yes if a paper is used |
| “模仿这 4 篇论文的 Discussion 逻辑” | `REQUIRED` | Named papers first | Yes | Mandatory |
| Grammar-only, citation-format-only, typo, single-caption micro-edit | `SKIP` | No | Existing lint route | Not required |

## Scientific contract

Both clients must:

- keep author text/data, verified results, and verified literature as the evidence boundary;
- treat numbers, formulas, variables, citations, effect directions, and sample sizes as protected content;
- preserve observational versus causal design boundaries;
- report `ABSTRACT_ONLY` or `METADATA_ONLY` honestly;
- use the official journal format before a soft abstract preference;
- prioritize core Results while retaining scientifically necessary results;
- use language tools for clarity, naturalness, argument rhythm, and author voice, not detection evasion;
- keep `PROVENANCE_METADATA_AUTO_STRIP = NO`.

## Verification notes

The executable golden set is stored at `skills/agent-auto-sci-scicomm/tests/writing_exemplar_golden_set.json` and is checked by `scripts/validation/validate_writing_exemplar_routing.py`. A parity failure means the clients disagree on mode, selection logic, read-scope claims, owner handoff, or anti-copying behavior; tool differences alone are not a failure.
