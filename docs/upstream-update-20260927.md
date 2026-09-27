# Upstream Update Audit - 2026-09-27

本次审计针对仓库中已经登记的外部 skill 来源和参考项目执行。目标是确认上游是否有新提交、判断是否属于本地封装范围，并在许可证和本地领域边界允许的情况下同步内容。

## 结论摘要

| 来源 | 本次检查到的提交 | 本地动作 | 结论 |
|---|---|---|---|
| [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | `49c6e97775eaa18ba791bebe23162a70ae601c18` | 未新增文件 | 当前四个精选 wrapper 的已封装目录相对 `c1ed16d` 没有内容变化。 |
| [Imbad0202/academic-research-skills-codex](https://github.com/Imbad0202/academic-research-skills-codex) | `3c37ef8ab480ba1e9370309c24b99977ad44091f` | 已同步 | 本地 ARS Codex package 更新到 `v3.22.0`；ARS source commit 为 `3c546bc08c56f79e0068f1ea4f0acedf5bf69b5e`。 |
| [skyllwt/AutoSci](https://github.com/skyllwt/AutoSci) | `cf88930d59ce8eb60d2080e1e9824cae333c0d8b` | 未复制 | 仅作参考源；上游此前的 GitHub hosted `requests` 依赖指针已恢复，本地原创 router 和 requirements 保持不变。 |
| [Haojae/scipilot-writing-skill](https://github.com/Haojae/scipilot-writing-skill) | `51c5fd39e2a386b7ddca021181b4c8071d3c3da7` | 无需同步 | 当前本地封装已与上游检查结果一致。 |
| [Haojae/scipilot-figure-skill](https://github.com/Haojae/scipilot-figure-skill) | `43098ddb9e6a6d142218540c114f9ed38922fc42` | 无需同步 | 当前本地封装已与上游检查结果一致。 |
| [xiangyu-Ge/sci-writing-geors](https://github.com/xiangyu-Ge/sci-writing-geors) | `1f58c002b5c11fe8a893dd74b3986e0bb3c1f2f2` | 无需同步 | 上游无新提交；本地继续使用原创 `geors-sci-writing-adapter`，不复制未明确授权的上游正文。 |

## 已同步内容

`academic-research-suite` 位于：

`skills/urban-exposure-review-radar-workflow/subskills/academic-research-suite`

本次同步更新了 ARS 的 `agents/`、`ars/`、`codex/`、根 `SKILL.md` 和 `manifest.json`，并保留本地分发所需的 `LICENSE`、`NOTICE.md`、`VERSION` 和嵌套拓扑实验运行目录。

本地版本为 `3.22.0`。由于 ARS 被作为独立嵌套子 skill 分发，质量门控脚本保留了本地适配：正确解析嵌套 manifest，且在缺少 Desktop plugin 的 standalone 包中跳过仅针对该插件或仓库级拓扑实验的 gate；其余 skill-level gate 不被绕过。

## 许可证与边界

- ARS 继续保留 CC BY-NC 4.0 许可证、来源说明和版本记录。
- K-Dense wrapper 继续保留 MIT 许可证和上游来源。
- SciPilot Writing、SciPilot Figure 继续保留 MIT 许可证和本地 NOTICE。
- GeoRS 上游未检测到明确 LICENSE，因此本地只保留来源链接和原创适配，不 vendoring 上游文本或代码。
- AutoSci 继续作为参考项目，不覆盖本地原创科研 router，也不引入其外部依赖指针。
- 本次没有把 K-Dense 精选范围之外的新 skill 导入仓库。

## 文档更新

同步刷新了：

- `README.md`
- `README_EN.md`
- `docs/skill-map.md`
- `docs/external-skills.md`
- `site/index.html`
- `site/agent-auto-sci-evolution.html`
- `CHANGELOG.md`

本地导航页现在统一显示整理版本 `0.9.0`、ARS `v3.22.0` 和本次上游检查日期 `2026-09-27`。
