# Agent Auto Sci Skills

> Geography + sport science research skills for Codex.

面向地理学 + 体育学交叉研究的本地科研 Agent Skills。这个项目把体育公园、体育设施、绿地/绿色暴露、热暴露、空间公平、城市健康、综述写作、系统综述、scoping review、文献计量分析、GIS/遥感、数据可视化、机器学习与 SCI 写作等工作流，整理成可复用的 Codex skills。

它不是一个“万能论文助手”。更准确地说，它是一套能持续积累、反复调用、逐步进化的科研工作流工具箱。

---

## 为什么做这个项目

在体育地理、城市健康与环境暴露研究里，一个研究问题往往不会只停留在“写一段论文”：

- 需要从 WoS/Scopus 等数据库设计检索式，并做系统综述或文献计量；
- 需要处理 GIS、遥感、空间可达性、绿色暴露、热暴露和地图合规；
- 需要做 EDA、统计检验、机器学习、SHAP/XAI 和稳健性分析；
- 需要把图、表、证据和政策建议组织成 Cities、SCS、UFUG、Environment International、Nature Cities 等期刊能接受的论证；
- 更重要的是，需要把失败经验、审稿意见、薄弱证据和写作规则保存下来，而不是每篇文章都从零开始。

本项目的核心思路是：

```text
sources -> structured memory -> idea and method design -> data/geo/ML analysis -> manuscript or review -> critique/rebuttal -> evolution archive
```

---

## 我们做了什么

- **科研 Agent 总控**：用 `agent-auto-sci` 统筹任务路由、长期记忆和 skill 进化。
- **综述与文献计量**：为 systematic review、scoping review、bibliometric analysis、critical coding 和 policy agenda 提供完整工作流。
- **体育地理实证写作**：把 sport park / sport facility / green exposure / heat exposure / equity / urban health 研究转成 SCI 论文叙事链。
- **GIS 与遥感**：沉淀 CRS、矢量/栅格、网络可达性、LCZ、NDVI/LST、地图合规和空间公平检查。
- **数据与图表**：建立 EDA、统计、图件、文献计量图、政策矩阵和 caption 规则。
- **AI/ML 与方法论**：强调 baseline、泄露检查、空间验证、SHAP 非因果边界、证据强度和偏倚审计。
- **科学交流**：覆盖论文结构、claim-evidence map、审稿回复、PPT、海报和期刊适配。

---

## Skills 总览

### 总领与自动科研

| Skill | 用途 |
|---|---|
| `agent-auto-sci` | 科研 Agent 总控、子 skill 路由、长期记忆和进化档案维护 |
| `agent-auto-sci-automation` | source manifest、checkpoint、失败经验、API 安全边界和自动科研流程 |

### 方法、数据、空间与模型

| Skill | 用途 |
|---|---|
| `agent-auto-sci-methodology` | 研究问题、假设、证据分级、偏倚审计和空间正义框架 |
| `agent-auto-sci-geospatial` | GIS、遥感、可达性、绿地/热暴露、空间公平和地图合规 |
| `agent-auto-sci-data-viz` | EDA、统计分析、论文图表、文献计量图和政策矩阵 |
| `agent-auto-sci-ai-ml` | 机器学习、SHAP/XAI、模型评估、空间/时间泄露检查和可复现性 |

### 写作、综述与体育地理

| Skill | 用途 |
|---|---|
| `agent-auto-sci-scicomm` | 科学写作、图文叙事、投稿、审稿回复、PPT 和海报 |
| `sport-geography-review-bibliometric` | 体育地理综述、系统综述、scoping review、文献计量、批判性编码和政策议程 |
| `sport-geography-sci-writing` | 体育地理实证 SCI 写作、目标期刊适配、图表和讨论 |

---

## 典型使用场景

### 1. 系统综述 + 文献计量 + 政策议程

适合主题：

- sport park exposure
- sport facility accessibility
- green exposure
- heat exposure
- park equity
- active-living infrastructure
- urban health
- environmental justice

推荐 skill 组合：

```text
agent-auto-sci
+ sport-geography-review-bibliometric
+ agent-auto-sci-methodology
+ agent-auto-sci-data-viz
+ agent-auto-sci-scicomm
```

### 2. 体育设施可达性与空间公平实证论文

推荐 skill 组合：

```text
agent-auto-sci
+ sport-geography-sci-writing
+ agent-auto-sci-geospatial
+ agent-auto-sci-data-viz
+ agent-auto-sci-methodology
```

### 3. GIS / 遥感 / 暴露评估

推荐 skill 组合：

```text
agent-auto-sci-geospatial
+ agent-auto-sci-data-viz
+ sport-geography-sci-writing
```

### 4. 论文投稿前自检

推荐 skill 组合：

```text
agent-auto-sci-scicomm
+ agent-auto-sci-methodology
+ sport-geography-sci-writing
```

---

## 安装方法

把本仓库的 `skills/` 复制到 Codex skills 目录：

```powershell
.\scripts\install.ps1
```

默认安装到：

```text
$env:USERPROFILE\.codex\skills
```

也可以指定目录：

```powershell
.\scripts\install.ps1 -Target "$env:USERPROFILE\.agents\skills"
```

安装后重启 Codex，让 skill 列表刷新。

---

## 公开安全原则

本仓库不应包含：

- API key、token、cookie、password；
- 私有 PDF 全文；
- 未发表论文正文；
- 审稿意见原文；
- WoS/Scopus 原始付费数据；
- 带个人身份的本地绝对路径；
- 用户自己的文献库、数据集和图件源文件。

发布前运行：

```powershell
.\scripts\scan_public_safety.ps1
```

---

## 第三方项目

本项目参考了多个优秀开源项目的结构和思路。第三方项目不整包随仓库分发，只在文档中作为可选扩展和学习来源列出。见 [docs/external-skills.md](docs/external-skills.md)。

---

## License

MIT License。若未来引入第三方源码，请逐一核对许可证并保留 attribution。
