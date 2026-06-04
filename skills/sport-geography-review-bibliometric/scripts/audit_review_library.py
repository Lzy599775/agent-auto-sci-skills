# -*- coding: utf-8 -*-
"""Audit a sport geography review literature library."""

from pathlib import Path
import argparse
import json

import pandas as pd


EXPECTED = {
    "readme": "00_文献库说明与变更记录.md",
    "workbook": "00_表格与清单/中文分类整理总表_含PDF匹配与下一步路线.xlsx",
    "strict": "00_表格与清单/严格Q1Q2与顶刊预筛表_268篇.csv",
    "manual": "00_表格与清单/严格非OA手动下载清单_48篇.csv",
    "pdf_dir": "01_非OA文献PDF/00_未整理_新下载PDF",
    "match": "02_PDF文本提取与匹配索引/PDF匹配与主题分类初稿.csv",
    "structure": "02_PDF文本提取与匹配索引/全文结构索引_48篇.csv",
}


def count_pdfs(path):
    if not path.exists():
        return 0
    return len(list(path.glob("*.pdf")))


def read_csv_rows(path):
    if not path.exists():
        return None
    return len(pd.read_csv(path, encoding="utf-8-sig"))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("library", help="Path to review_literature_library")
    args = parser.parse_args()
    base = Path(args.library).resolve()

    report = {
        "library": str(base),
        "exists": base.exists(),
        "files": {},
        "counts": {},
        "warnings": [],
    }
    for key, rel in EXPECTED.items():
        path = base / rel
        report["files"][key] = {"path": str(path), "exists": path.exists()}

    report["counts"]["pdf_count"] = count_pdfs(base / EXPECTED["pdf_dir"])
    for key in ["strict", "manual", "match", "structure"]:
        rows = read_csv_rows(base / EXPECTED[key])
        report["counts"][f"{key}_rows"] = rows

    if report["counts"]["pdf_count"] and report["counts"]["manual_rows"]:
        if report["counts"]["pdf_count"] != report["counts"]["manual_rows"]:
            report["warnings"].append("PDF count does not match manual-download table rows.")

    if report["counts"]["match_rows"] and report["counts"]["manual_rows"]:
        if report["counts"]["match_rows"] != report["counts"]["manual_rows"]:
            report["warnings"].append("PDF match table rows do not match manual-download table rows.")

    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()


