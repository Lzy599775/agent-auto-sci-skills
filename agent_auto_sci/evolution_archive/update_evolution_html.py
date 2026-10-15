"""Render the compact public evolution archive from evolution_data.json."""

from __future__ import annotations

import html
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
DATA_PATH = HERE / "evolution_data.json"
OUTPUT_PATH = HERE / "agent-auto-sci-evolution.html"


def render(data: dict) -> str:
    capabilities = "".join(
        "<article><h3>{}</h3><p>{}</p><p><strong>Why no new top-level skill:</strong> {}</p></article>".format(
            html.escape(item["name"]),
            html.escape(f"{item['owner']} · {item['role']}"),
            html.escape(item["why_no_new_top_level_skill"]),
        )
        for item in data.get("capabilities", [])
    )
    timeline = "".join(
        "<article><h3>{} · {}</h3><p>{}</p></article>".format(
            html.escape(item["date"]),
            html.escape(item["title"]),
            html.escape(item["summary"]),
        )
        for item in data.get("timeline", [])
    )
    checks = "".join(
        "<li><code>{}</code>: {}</li>".format(html.escape(str(key)), html.escape(str(value)))
        for key, value in data.get("validation", {}).items()
    )
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Agent Auto Sci evolution archive</title>
  <style>
    :root {{ color-scheme: dark; }}
    body {{ max-width: 960px; margin: 0 auto; padding: 2rem; font: 16px/1.6 system-ui, sans-serif; background: #11161b; color: #eef3f0; }}
    article {{ margin: 1rem 0; padding: 1rem 1.2rem; border: 1px solid #334155; border-radius: .5rem; background: #182027; }}
    h1, h2 {{ color: #6ee7b7; }}
    code {{ color: #bfdbfe; }}
  </style>
</head>
<body>
  <h1>Agent Auto Sci evolution archive</h1>
  <p>Updated {html.escape(str(data.get("updated", "NOT_REPORTED")))}.</p>
  <h2>Capabilities</h2>
  {capabilities}
  <h2>Timeline</h2>
  {timeline}
  <h2>Validation</h2>
  <ul>{checks}</ul>
</body>
</html>
"""


def main() -> None:
    data = json.loads(DATA_PATH.read_text(encoding="utf-8"))
    OUTPUT_PATH.write_text(render(data), encoding="utf-8", newline="\n")
    print(OUTPUT_PATH)


if __name__ == "__main__":
    main()
