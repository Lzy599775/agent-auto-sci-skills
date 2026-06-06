from __future__ import annotations

import argparse
from pathlib import Path


DIRS = [
    "00_项目说明",
    "01_search检索",
    "02_screening筛选",
    "03_extractions提取",
    "04_synthesis综合",
    "05_outline大纲",
    "06_draft草稿",
    "07_manuscript投稿稿",
    "08_references引用",
    "09_audit质量门控",
    "10_frontier_radar前沿雷达",
]


README = """# Review Radar Project

## Project Positioning

- Review type:
- Target journal route:
- Core contribution:
- Databases:
- Search date:
- Frontier radar date:

## Rules

- Keep formal review corpus and frontier radar candidates separate.
- Do not store API keys or private credentials in this folder.
- Every factual claim in the manuscript must map to extraction notes or verified sources.
"""


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("output_dir", help="Project output directory")
    args = parser.parse_args()

    root = Path(args.output_dir)
    root.mkdir(parents=True, exist_ok=True)
    for name in DIRS:
        (root / name).mkdir(exist_ok=True)

    readme = root / "00_项目说明" / "README_项目定位.md"
    if not readme.exists():
        readme.write_text(README, encoding="utf-8")

    templates = {
        "02_screening筛选/筛选记录模板.csv": "id,title,doi,year,database,stage,decision,reason,notes\n",
        "03_extractions提取/提取字段模板.csv": "id,title,object,exposure_metric,accessibility_metric,spatial_scale,population,outcome,method,confounders,effect_direction,limitations,claim_evidence_notes\n",
        "10_frontier_radar前沿雷达/候选论文项目评分表.csv": "rank,title,source,date,task,data_modality,contribution,code_data_status,novelty,evidence,reproducibility,transferability,user_fit,total_score,why_it_matters\n",
        "09_audit质量门控/claim_evidence_map.md": "# Claim-Evidence Map\n\n| Claim | Source | Evidence | Risk | Status |\n|---|---|---|---|---|\n",
    }

    for rel, content in templates.items():
        path = root / rel
        if not path.exists():
            path.write_text(content, encoding="utf-8")

    print(f"Created review radar scaffold at: {root}")


if __name__ == "__main__":
    main()

