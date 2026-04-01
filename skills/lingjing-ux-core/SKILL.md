---
name: lingjing-ux-core
description: UX skill for Lingjing Aviation Intelligence Platform, defining interaction patterns, flows, and scenario configs for 2D products (B-system, website, dashboard, presentation) and UE5 Web Overlay / digital-twin information layers.
license: MIT
compatibility: [Claude, GPT-4, Cursor, CodeBuddy]
metadata:
  version: 1.0.0
  updated: 2026-03-25


  author: Lingjing UX System Team
  category: UX Design Skill
  language: zh-CN
---

# ✈️ LingJing UX Core - 航空工业智能平台 UX 技能包

> **技能定位**：为 AI 提供“可执行的交互规范”，补足仅有 UI 组件时的行为与流程空白。
> **适用范围**：二维产品界面（网站、B 端系统、HTML 演示文稿、仪表盘等）。
> **核心版本**: v1.0.0


---

## 0. 核心执行规约 (Core Execution Protocol - 必须遵循)

### 0.0.1 强制任务清单 (Atomic Task Template)
AI 在执行 UX 设计任务时，**必须**按以下原子步骤进行规划：
1. **[分析] 整理请求**：读取需求并整理为 `design_request` [Evidence Required]。
2. **[取证] 检索规范**：检索并读取 `modes/` 或 `scenes/` 中的参考规范文件 [Evidence Required]。
   - 若场景为“UE5 Web Overlay / 数字孪生叠加层”，需同步读取 `patterns/web_overlay_runtime.yml` 或 `scenes/ue5_factory_overlay_scene.yml`，并在后续 UI 阶段默认指向 `lingjing-core-ue5-overlay.css`（如需后台导航/表格/表单再叠加 `lingjing-core-b-system.css`）。
3. **[定义] 确定结构**：确定核心任务流 `flows` 与页面区域划分 `pages`。
4. **[建模] 产出规约**：编写并校对完整的结构化 `ux_spec` (YAML)。
5. **[落盘] 交付产物**：将 `ux_spec` 写入目标项目目录（如 `docs/ux/` 或 `specs/ux/`）。
6. **[移交] 准备摘要**：输出 3-5 行摘要说明场景、模式与关键交互点，供 UI 技能消费。


### 0.0.2 行为黑名单 (Negative Constraints)
- **禁止口头协议**：严禁在回复中说“已遵循规范”但未产出结构化 YAML 文件。
- **禁止路径漂移**：产物必须落在用户工作区，严禁写回技能包自身目录。
- **禁止凭空生成**：在输出 `ux_spec` 前，必须展示已读取的参考模式或场景文件路径。

### 0.0.3 验证/验收模式 (Audit Mode)
当需求包含“验证/验收/复现/对标/跑通/检查技能包”时：
- 必须完整包含 `design_request / scene / flows / pages / navigation / dev_handoff`。
- **强制需求驱动取用 (Demand-Driven Selection)**：禁止为了“凑数”而机械堆叠模式或场景；UX 方案必须与业务 PRD 的功能点一一对应，允许单场景直推或多模式片段编排，以 `prd_module_coverage_score` 为核心评价标准。
- **输出增强审计字段 (Enhanced Audit Fields)**：最终摘要必须包含：`prd_module_coverage_score` (PRD 覆盖率)、`ux_flow_integrity_score` (交互流闭环度)、`template_similarity_score` (模板同构风险)。
- UI 阶段开始前，必须确认 `ux_spec` 已成功落盘。


---

## 1. 协作模式与落点规则

### 1.1 结构化落点规则
- 优先路径：`docs/ux/ux_spec_<scene>.yml` 或 `specs/ux/ux_spec_<scene>.yml`。
- 前端项目优先：`src/ux/ux_spec_<scene>.yml`。
- 禁止只给 Markdown 说明；若有 `.md` 文档，仅作为辅助。

### 1.2 UX → UI 协同关键信息
在编写 `ux_spec` 时，必须确保以下字段清晰：
- `pages[*].route_path`: 表达页面的业务路由 / 访问路径，不等于真实文件落点；UI 最终写入哪个文件，应由调用方项目结构决定。
- `pages[*].priority`: 页面优先级，取值 `high | medium | low`。PRD 中 P0/P1 模块所在页面应标注 `priority: high`；UI 阶段据此判定 `delivery_scope: partial` 时，核心交付范围为所有 `priority: high` 页面。示例：
  ```yaml
  pages:
    - id: dashboard
      route_path: /dashboard
      priority: high   # P0 核心页，必须优先交付
    - id: settings
      route_path: /settings
      priority: medium
  ```
- `dev_handoff.output_file_hint`: 可选；仅在已知调用方工程目录约束时填写，用于提示 UI 更稳妥的文件落点。
- `component_roles[*].lingjing_core_class`: 决定 UI 命中的关键组件类；其取值必须来自 `lingjing-ui-core` 已存在的 canonical 类名（优先参考 `scene_coverage_matrix.yml.canonical_class_contract`，其次参考 `CLASS_NAME_REFERENCE.md` 或 `components/dist/*.css`），禁止在 UX 层发明新的类名期待 UI 实现对应样式。**落盘前必须运行类名校验**：
  ```
  node scripts/ux-spec-lint.js <ux_spec.yml>
  ```
  - FAIL（含 ERROR 项）：禁止将此 ux_spec 传递给 UI 落地；修复后重跑。
  - WARN（alias/deprecated）：运行 `--fix` 自动归一化后再落盘，或手动替换。
  - PASS：类名校验通过，可交 UI 落地。
- `action_targets[*].target_id` / `navigation.*.target_id`: 统一表达跳转或联动目标；其语义由 `target_type` 决定（如 `page / drawer / modal / anchor`），避免继续混用 `target_page_id` 表示抽屉或锚点。
- `navigation`: 定义入口页、页面跳转路径及全局导航项。
- `pages[*].zones`: 若涉及 B 端顶部栏 + 左侧菜单、网站顶部栏、UE 顶部 HUD 等框架层，应默认遵循 UI Skill 的强一致骨架，不将其作为项目差异化重点。**（可选但推荐）** 若当前环境可访问 `lingjing-ui-core/scene_coverage_matrix.yml`，在定义 zones 和框架层结构时参考其 `shell_consistency`，可避免后续 UI 阶段被 skill-audit 拦截。

> 若业务确实需要当前技能包未覆盖的视觉形态，应在 `dev_handoff.edge_cases_zh` 中明确记录“需要业务项目在灵境样式之上扩展”的说明，而不是在 `lingjing_core_class` 中填入不存在的类名；若引用了历史别名，必须在最终 `ux_spec` 落盘前归一化为 canonical 类名。为兼容历史产物，可暂时保留 `target_page_id`，但新输出应统一写 `target_id`。

---


## 2. 交互维度与模式

本技能包将交互空间拆分为“产品场景 × 交互维度”：

- **产品场景**：`website` (营销), `b-system` (管理), `presentation` (演示), `ai-assistant` (助手), `ops-console` (监控), `ue5_web_overlay` (UE5 叠加层).
- **交互维度**：`data_intelligence` (智能数据), `business_process` (流程审批), `security_compliance` (安全合规).

**`product_scene` → UI `scene_id` 映射表**（`scene_id` 须与 `scene_coverage_matrix.yml` 及 `skill-audit --scene` 保持一致）：

| `product_scene`（UX 层） | `scene_id`（UI 层） | 备注 |
|---|---|---|
| `b-system` | `b_system` | 后台管理、作业系统、驾驶舱 |
| `ops-console` | `b_system` | 监控大屏复用 B 端组件体系 |
| `website` | `website` | 营销/企业门户 |
| `presentation` | `presentation` | 演示文稿 |
| `ai-assistant` | `b_system` | AI 工作台复用 B 端样式入口 |
| `ue5_web_overlay` | `ue5_overlay` | UE5 Web Overlay / 数字孪生叠加层 |

### 3.0 典型交互模式 (Modes)
- `real_time_monitor`: 实时监控，高频刷新，预警驱动。
- `multi_level_approval`: 多级审批，状态流转，审计跟踪。
- `exception_handling`: 异常处理，阻断性交互，修复指引。
- `web_overlay_runtime`: UE5 Web Overlay 运行模式，统一桥接、降级、指针穿透与性能约束。
- `world_space_ui`: 世界空间 UI / 轻量锚点模式，强调三维对象与二维详情层联动。 

### 3.1 UE5 Web Overlay 场景专用约束
- 当 `design_request.product_scene` 为 `ue5_web_overlay` 或 `scene.mode_id` 为 `web_overlay_runtime` / `world_space_ui` 时：

  **[框架层强制声明]** 以下两个框架层组件与 B 端的顶部栏 + 侧边菜单地位等同，属于强一致骨架，**默认必须包含在 `ux_spec` 中**：
  - `ue5-overlay-system-bar`（系统顶部导航栏）：**必须包含**，除非 PRD 中明确写有"无顶部导航"或"仅三维场景全屏无 UI 框架"。注意：去掉"顶部数据卡片/状态卡"并不等于去掉系统栏，两者是不同层级。
  - `ue5-overlay-bottom-dock`（底部停靠区）：有时间轴或快捷操作时包含，无需求时可省略。

  **[取证] 降级链（按顺序尝试，成功即止）：**
  1. 读取 `patterns/web_overlay_runtime.yml` 或 `scenes/ue5_factory_overlay_scene.yml` → 成功则继续
  2. 若以上文件不可访问，改为读取 `lingjing-core-ue5-overlay.css` 提取类名列表 → 成功则继续
  3. 若 CSS 也不可访问，**直接使用下方 §3.1.canonical 内联类名表**作为唯一合法来源 → 继续
  4. 若三者均失败，停止并说明”当前环境无法获取任何 UE5 Overlay 类名参考，请用户提供文件路径或内容”，**不得输出** `ux_spec`

  > 降级链允许在无文件访问权限的环境（如 IDE 沙箱、远程 AI Builder）中继续工作，但必须在产物摘要中注明”取证来源：§3.1.canonical 内联表”。

  - `pages[*].component_roles[*].lingjing_core_class` 必须**只能**选自 `lingjing-core-ue5-overlay.css` 已存在的类名集合（见 §3.1.canonical），禁止使用 PRD、需求文档或自行推断的”预期类名”；禁止使用 `.lj-overlay-*`、`.ue5-data-card`、`.ue5-timeline-*`、`.status-badge--*` 等新前缀或不存在的类名。
  - 对于当前技能包尚未覆盖的业务控件，只允许在 `dev_handoff.edge_cases_zh` 中提出”由业务项目在 overlay 样式之上扩展”，并使用 §3.2 三级扩展策略（项目前缀 `pj-ue5-*`）。

#### §3.1.canonical UE5 Overlay 规范类名速查表

> 此表为 `lingjing-core-ue5-overlay.css` 已存在类名的功能分组摘要，是 UE5 场景 `lingjing_core_class` 的**唯一合法来源**。

**① 结构层**

| 类名 | 用途 |
|------|------|
| `ue5-overlay-root` | 整个叠加层根容器 |
| `ue5-overlay-background` | 深色背景层 |
| `ue5-overlay-viewport` | 三维场景视口透传区 |
| `ue5-overlay-grid` | 网格辅助线层 |
| `ue5-overlay-center-guard` | 中央保护区（防遮挡） |
| `ue5-overlay-safe-area` | 安全区内容容器 |
| `ue5-overlay-panel` | 通用面板基类（玻璃透明效果） |
| `ue5-overlay-layer` | 层叠修饰基类 |
| `ue5-overlay-layer--hud` | HUD 层（高频操作区） |
| `ue5-overlay-layer--detail` | 详情层（侧面板内容区） |
| `ue5-overlay-layer--marker` | 世界标记层 |
| `ue5-overlay-layer--critical` | 告警层（最高优先级） |
| `ue5-overlay-bottom-dock` | 底部停靠栏容器（时间轴/快捷操作） |
| `ue5-overlay-dock-group` | 停靠栏按钮组 |
| `ue5-overlay-dock-button` | 停靠栏按钮 |
| `ue5-overlay-dock-status` | 停靠栏状态指示 |
| `ue5-overlay-dock-time` | 停靠栏时间显示 |

**② 顶栏 HUD（有顶栏场景使用；无顶栏场景省略）**

| 类名 | 用途 |
|------|------|
| `ue5-overlay-system-bar` | 系统顶栏容器 |
| `ue5-overlay-system-bar__brand` | 品牌区块 |
| `ue5-overlay-system-bar__brand-name` | 系统名称文字 |
| `ue5-overlay-system-bar__brand-subtitle` | 副标题文字 |
| `ue5-overlay-system-bar__nav` | 导航容器 |
| `ue5-overlay-system-bar__nav-item` | 导航项 |
| `ue5-overlay-system-bar__meta` | 元信息区（时间/状态） |
| `ue5-overlay-system-bar__meta-item` | 元信息项 |
| `ue5-overlay-system-bar__meta-dot` | 状态点 |
| `topbar-hud` | 顶部 HUD 信息条（宽屏横向） |
| `topbar-hud--with-sidepanel` | 有侧面板时的 HUD 变体 |
| `topbar-hud--compact` | 紧凑 HUD |
| `topbar-hud--quality` | 质量专用 HUD |
| `topbar-hud__title` | HUD 主标题 |
| `topbar-hud__subtitle` | HUD 副标题 |
| `topbar-hud__stat` | 关键指标单元 |
| `topbar-hud__stat--success/warning/critical/info/brand` | 指标状态修饰 |
| `topbar-hud__stat-value` | 指标大字 |
| `topbar-hud__stat-label` | 指标标签 |
| `topbar-hud__stat-meta` | 指标说明 |
| `topbar-hud__status` | 当前焦点状态 |

**③ 侧面板 detail-panel（左/右侧面板主体）**

| 类名 | 用途 |
|------|------|
| `detail-panel` | 侧面板容器基类 |
| `detail-panel--pinned` | 固定面板修饰 |
| `detail-panel--stale` | 数据陈旧状态 |
| `detail-panel--error` | 错误状态面板 |
| `detail-panel__header` | 面板头部 |
| `detail-panel__title-group` | 标题组 |
| `detail-panel__title` | 面板标题 |
| `detail-panel__eyebrow` | 小标签/场景标注 |
| `detail-panel__meta` | 元信息（时间、说明等） |
| `detail-panel__status` | 状态标签 |
| `detail-panel__body` | 面板主体内容区 |
| `detail-panel__section` | 内容分区 |
| `detail-panel__section-title` | 分区标题 |
| `detail-panel__metrics` | 指标组容器 |
| `detail-panel__metric` | 单个指标 |
| `detail-panel__metric--success/warning/critical/brand` | 指标状态修饰 |
| `detail-panel__metric-value` | 指标大字数值 |
| `detail-panel__metric-label` | 指标标签 |
| `detail-panel__metric-meta` | 指标说明 |
| `detail-panel__list` | 列表容器 |
| `detail-panel__list-row` | 列表行 |
| `detail-panel__list-label` | 行标签 |
| `detail-panel__list-value` | 行数值 |
| `detail-panel__assist` | 辅助说明文字 |
| `detail-panel__fold` | 折叠区 |
| `detail-panel__fold-summary` | 折叠触发项 |
| `detail-panel__fold-body` | 折叠内容 |
| `detail-panel__footer` | 面板底部操作区 |
| `detail-panel__footer-action` | 底部操作按钮 |
| `detail-panel__footer-action--primary` | 主要操作按钮 |

> **`ue5-critical-banner` 条件显示规范**：告警横幅仅在告警激活时出现。隐藏时必须使用 `display:none`（禁止用 `visibility:hidden`），以保证 `detail-panel__body` 能通过 `flex:1` 填满剩余高度，不留空白。在 `ux_spec.component_roles` 中，若告警横幅为条件组件，需在 `description` 中注明"无告警时 display:none"；在 `dev_handoff.edge_cases_zh` 中说明切换逻辑。

> **`ue5-overlay-status` 修饰符说明**（区别于 B 端 `badge`）：UE5 状态徽章使用 BEM 双破折号修饰符，格式为 `ue5-overlay-status--success/warning/critical/info`，**这是正确写法**。无对应状态的"待开始/idle"直接使用不带修饰符的 `ue5-overlay-status`（默认灰色）即可，无需自造 `--idle`。B 端 `badge` 类才是单破折号（`badge-success`）。两套规则不相互适用。

**④ 图层切换面板 layer-switcher（左侧控制面板）**

| 类名 | 用途 |
|------|------|
| `layer-switcher` | 图层切换面板容器 |
| `layer-switcher__header` | 面板头部 |
| `layer-switcher__title` | 面板标题 |
| `layer-switcher__status` | 状态说明 |
| `layer-switcher__list` | 图层列表 |
| `layer-switcher__item` | 图层项 |
| `layer-switcher__item-title` | 图层名称 |
| `layer-switcher__item-meta` | 图层说明 |
| `layer-switcher__item-tag--critical/info/success` | 图层类型标签 |
| `layer-switcher__item-meter--critical/info/success` | 图层进度指示 |
| `layer-switcher__toggle` | 开关按钮 |
| `is-on` / `is-syncing` | 开启/同步状态 |

**⑤ 告警组件**

| 类名 | 用途 |
|------|------|
| `ue5-critical-banner` | 全局关键告警横幅（红色）|
| `ue5-critical-banner__title` | 横幅标题 |
| `ue5-critical-banner__copy` | 横幅说明 |
| `ue5-critical-banner__pill` | 告警标签 |
| `ue5-critical-banner__actions` | 操作按钮组 |
| `ue5-critical-banner__action` | 操作按钮 |
| `ue5-critical-banner__action--primary` | 主要操作 |
| `alert-center` | 告警中心面板 |
| `alert-center__severity--warning/critical/info/success` | 告警严重级别 |
| `alert-center__drawer--critical/warning/info` | 告警抽屉 |
| `alert-center__summary-card--critical/info` | 汇总卡片 |

**⑥ 状态指示**

| 类名 | 用途 |
|------|------|
| `ue5-overlay-status` | 状态徽章基类 |
| `ue5-overlay-status--success` | 成功/已完成 |
| `ue5-overlay-status--warning` | 警告/风险 |
| `ue5-overlay-status--critical` | 错误/超限 |
| `ue5-overlay-status--info` | 进行中/信息 |
| `ue5-status-indicator` | 状态指示器 |
| `ue-status-active` / `ue-status-warning` / `ue-status-error` / `ue-status-idle` | 运行状态 |

**⑦ 数据可视化**

| 类名 | 用途 |
|------|------|
| `chart-placeholder` | 图表占位容器（含渐变背景，ECharts 挂载目标） |
| `charts-grid--single` | 单列图表网格（UE5 侧面板必须用此，禁用默认2列） |
| `quality-meter` | 进度条/负载条 |
| `quality-meter--dominant/high/medium/low` | 进度条强度修饰 |
| `timeline-histogram` | 时间轴直方图 |
| `timeline-label` | 时间轴标签 |
| `card-ue-data` | 数据卡片（轻量） |
| `card-ue-data-highlight` | 高亮数据卡片 |

**⑧ 时间轴（垂直步骤式）**

> 注：CSS 中无独立的水平生产里程碑时间轴组件。垂直步骤式时间轴可使用以下类；水平时间轴需通过 §3.2 三级扩展（`pj-ue5-*` 前缀）实现，并在 `dev_handoff.edge_cases_zh` 中说明。

| 类名 | 用途 |
|------|------|
| `quality-closure-panel__timeline` | 垂直时间轴容器 |
| `quality-closure-panel__timeline-step` | 时间轴步骤项 |
| `quality-closure-panel__timeline-step--critical` | 关键/阻断步骤 |
| `quality-closure-panel__timeline-step--warning` | 风险步骤 |
| `quality-closure-panel__timeline-step--info` | 正常/已完成步骤 |
| `quality-closure-panel__timeline-head` | 步骤头部 |
| `quality-closure-panel__timeline-status` | 步骤状态标签 |
| `quality-closure-panel__timeline-meta` | 步骤说明 |

**⑨ 世界标记**

| 类名 | 用途 |
|------|------|
| `world-marker` | 三维场景锚点标注基类 |
| `world-marker--critical` | 关键问题标记（红色高亮） |
| `world-marker--warning` | 警告标记 |
| `world-marker--info` | 信息标记 |
| `world-marker--selected` | 选中状态 |
| `world-marker--collapsed` | 收起状态（远景） |
| `world-marker__card` | 标记弹出卡片 |
| `world-marker__title` | 卡片标题 |
| `world-marker__status` | 状态标签 |
| `world-marker__action` | 操作按钮 |

**⑩ 交互工具**

| 类名 | 用途 |
|------|------|
| `ue-tooltip` | 悬停提示框（注意：`ue-` 前缀，非 `ue5-`） |
| `ue-focus-banner` | 处置建议横幅 |
| `ue-focus-banner__title` | 横幅标题 |
| `ue-focus-banner__content` | 横幅内容 |
| `ue5-overlay-section-title` | 区域分节标题 |
| `ue5-overlay-subcard` | 子卡片 |

### 3.2 UE5 Overlay 组件不足时的扩展策略
- **一级：内容扩展**：在 `.detail-panel`、`.world-marker`、`.topbar-hud` 等官方组件内部，通过增加字段分组、说明区块、图表卡片等方式表达新增需求，不新增任何新的 overlay 组件类名。
- **二级：修饰符扩展**：当需要强调告警或关键状态时，可在官方组件类上叠加修饰符类（如 `detail-panel--alarm`、`world-marker--critical`），但这些类必须被标注为项目样式，只能出现在调用方项目 CSS 中，不可写入技能包 dist；在 `ux_spec.dev_handoff.edge_cases_zh` 中需说明这些修饰符的语义与作用区域。
- **三级：项目前缀组件**：确需全新组件时，只能定义带有项目前缀的类名（建议前缀如 `pj-ue5-`），并通过 `component_roles[*].lingjing_core_class` 指向其所基于的官方组件组合（例如 `.detail-panel` + `.chart-card`）；在 `dev_handoff.edge_cases_zh` 中必须明确记录这些项目组件的结构和交互假设，方便 UI 与前端落地。

#### §3.2.dom 三级扩展组件 DOM 骨架规范

当使用三级扩展（`pj-ue5-*`）设计新组件时，**必须**在 `dev_handoff.edge_cases_zh` 中提供 DOM 骨架说明，而不是只给类名和描述。骨架说明需包含：元素嵌套结构、关键 CSS 属性方向、连接元素（如时间轴的连接线）。

**强制要求：自定义组件 CSS 禁止硬编码任何颜色或透明度值**，必须引用 CSS Token（参见 `docs/css-token-reference.md` §二）。违反示例：
```css
/* ❌ 禁止 */
background: rgba(2,8,20,0.4);
border-color: rgba(79,141,245,0.15);
color: #02c39a;

/* ✅ 正确 */
background: var(--ue5-overlay-panel-bg);
border-color: var(--ue5-overlay-panel-border);
color: var(--ue5-overlay-success);
```

**常见新组件骨架范式**（在 `edge_cases_zh` 中提供对应结构）：

**横向时间轴**（水平里程碑轴线）：
```
DOM 结构：
  .pj-ue5-timeline                    ← flex-row 容器，overflow-x:auto
    .pj-ue5-timeline__track           ← 相对定位容器，承载轴线和节点
      .pj-ue5-timeline__line          ← 绝对定位横线（高1-2px，宽100%，贯穿所有节点）
      .pj-ue5-timeline__node × N      ← 各节点（含圆形标记 + 上方/下方标签）
        .pj-ue5-timeline__dot         ← 圆形标记（8-12px，颜色由状态决定）
        .pj-ue5-timeline__label       ← 节点名称（dot 上方或下方）
        .pj-ue5-timeline__date        ← 日期文字（比 label 字号更小）

关键 CSS 约束：
  - __line 需绝对定位 top:50%（或节点中心高度）
  - __node 用 flex-column + align-items:center
  - __dot 状态颜色：done→var(--ue5-overlay-success)，
                    active→var(--ue5-overlay-brand) + box-shadow 发光，
                    alert→var(--ue5-overlay-warning)，
                    future→var(--ue5-overlay-text-dim)
  - 连接线颜色：var(--ue5-overlay-panel-border)
```

**其他新组件**以相同格式提供，重点描述：父容器布局方向、关键子元素的定位方式、状态变化影响哪些属性。

### 3.2a 图表容器布局规范（B 端 + UE5 通用）
- **图表行容器**：使用 `charts-grid` 作为行容器；默认为 2 列（`minmax(400px, 1fr)`），窄容器（如 UE5 侧面板）**必须**叠加 `charts-grid--single` 强制单列，否则图表将溢出面板。
- **可用列数修饰符**：`charts-grid--single`（1列）/ `charts-grid--2`（2列）/ `charts-grid--3`（3列）/ `charts-grid--4`（4列）。UE5 侧面板宽度约 332px，只允许使用 `--single`。
- **B 端图表卡片嵌套规则**：`charts-grid > b-chart-card > b-chart-header + b-chart-body > <div id="chartXxx" style="height:Npx">`。ECharts 挂载目标为 `b-chart-body` 内的**普通 `<div>`**，禁止在 `chart-placeholder` 上挂载（该类含 UE5 专用渐变背景）。
- **content-card 嵌套禁忌**：`stats-grid` 和 `charts-grid` 直接放在 `b-content` 下，**禁止**嵌套在 `content-card` 内；`content-card` 仅用于表格/列表/表单等非图表区块。

### 3.2b B 端徽章与状态指示规范
- **徽章修饰符**：`badge` 为基类，修饰符使用**单破折号**：`badge-success` / `badge-warning` / `badge-error` / `badge-primary`；禁止使用双破折号写法（如 `badge--success`）。
- **状态点**：使用 `b-status-dot` + `b-status-dot--online` / `--idle` / `--offline` / `--error` 表示设备/服务在线状态，禁止用纯内联色点替代。

### 3.3 跨场景 UX 质量基线（按场景裁剪）
- **适用范围**：本节作为灵境通用 UX 质量基线，供所有场景参考；具体约束需结合场景裁剪，不改变现有设计系统的视觉基因。
- **执行方式**：在生成 `ux_spec` 时，应在 `ux_spec.dev_handoff.edge_cases_zh` 中记录与本节相关的风险与建议，UI 技能与业务前端在实现时据此进行样式与交互调优。

#### 3.3.1 通用基线（适用于所有场景）
- **可访问性基线**：
  - 关键文本（表头、数据卡片、按钮）应满足 AA 级对比度（≈4.5:1），如存在“品牌色过浅”等视觉要求，应在 `dev_handoff.edge_cases_zh` 中说明并提醒业务团队评估。
  - 重要信息不要只用颜色区分，应同时配合图标/文案（例如告警用图标+文字，而不是仅用红色）。
  - 表单与交互控件必须有清晰标签，不允许仅用 placeholder 代替 label。
- **触控与交互基线**：
  - 主要可点击区域（按钮、卡片、世界标注等）建议可点击区域不小于约 40–44px 的视觉尺寸，紧凑 B 端界面中如需减小，应在 `dev_handoff.edge_cases_zh` 中标注“触控风险”。
  - 所有可点击元素必须有明确的 hover/active/disabled 反馈；若某些状态由于产品限制无法实现，应在 `dev_handoff` 中说明。
- **布局与间距基线**：
  - 采用 4/8px 的间距节奏；重要模块间隔明显大于模块内部元素间隔，避免“所有间距都一样导致层次不清”。
  - 文本行长建议控制在可读范围内（桌面端内容区约 60–75 字符宽度），长文内容宜通过分段与子标题分层，而不是铺满全宽。
- **动效与反馈基线**：
  - 微交互（按钮按下、卡片浮起、告警出现/消失）的动效时长宜控制在 150–300ms 之间，过渡曲线应自然（ease-in/out），避免瞬闪或明显拖沓。
  - 必须考虑“低动效/性能有限设备”：若场景对 WebGL/三维负载已较重，应在 `dev_handoff` 中建议减少大面积装饰性动画。

#### 3.3.2 UE5 Web Overlay / 数字孪生叠加层专用基线
- **HUD 信息层次与遮挡控制**：
  - 在 `ux_spec.pages[*].component_roles` 中，应清晰区分 HUD 顶栏、告警中心、图层切换、世界标注详情面板等区域，避免出现多个高权重面板叠加遮挡核心视图。
  - 建议将 HUD/告警/图层切换等高频操作区域放在视口四角安全区，并保留中间大部分区域给三维场景本身；如确有遮挡需求，应在 `dev_handoff.edge_cases_zh` 中说明“视图遮挡预期”。
- **世界标注与可点性**：
  - `world-marker` 相关角色应考虑点击/悬停时的命中面积与视距变化对可见性的影响，可在 `dev_handoff` 中建议最小图标尺寸与文字展示策略（如远景只显示点+简短状态，近景展开更多信息）。
- **性能与加载反馈**：
  - 对于 overlay 内部的图表、列表、告警流等，应在 `flows` 中标出加载与错误路径（如 skeleton / 重试按钮），避免出现“空白卡片无反馈”。
  - 如三维场景本身已经存在明显渲染压力，建议在 `dev_handoff` 中注明“优先保证渲染帧率，减少 Overlay 装饰性动效”。

#### 3.3.3 B 端列表页 / 表格密度基线
- **信息密度与可读性平衡**：
  - 在 B 端场景下，`flows` 与 `pages` 中涉及表格的页面，应明确行高、列宽与关键字段数量，避免“表格行距过大导致信息密度不足”或“所有内容挤在一起难以阅读”。
  - 建议通过 `status-dot`、`badge` 等轻量视觉元素表达状态，保留足够空间给文本内容；如某些列表需要极高密度，可在 `dev_handoff` 中标记“高密度模式”，方便 UI 在实现时进行节奏调整。
- **层次结构与对齐**：
  - 重要操作（如主 CTA、批量操作）应集中在表格上方的 `table-toolbar` 区域或每行尾部，避免分散在多处导致用户决策困难。
  - 应明确说明是否需要“冻结首列/表头”、“行悬停高亮”等交互，以保证 UI 与前端在实现时不会各自猜测。

#### 3.3.4 官网 / 演示 / AI 工作台场景基线
- **官网 / 演示**：突出视觉冲击与叙事节奏，但仍需满足基础对比度与可读性；长页面应设计清晰的滚动锚点与分节结构。
- **AI 工作台**：
  - 消息流与工具面板布局应在 `pages` 中明确：例如 `chat-layout` 的主对话区、侧边工具栏、任务状态区域。
  - 建议在 `dev_handoff.edge_cases_zh` 中标注关键反馈点（如工具执行中的 loading / 成功 / 失败）、重要消息的强调方式（颜色 + 图标 + 标签），避免 UI 只停留在“有消息气泡”但缺少状态价值。

---

## 4. 标准输出结构 (ux_spec)




```yaml
ux_spec:
  design_request: { business_context_zh: "...", product_scene: "..." }
  scene: { id: "...", name_zh: "...", ux_goals_zh: ["..."] }
  flows: [{ id: "...", steps: ["..."] }]
  pages: [{ id: "...", route_path: "...", component_roles: [{ role: "...", lingjing_core_class: "...", mode_id: "..." }] }]
  navigation: { entry_page_id: "...", page_links: [] }
  dev_handoff: { api_expectations_zh: ["..."], edge_cases_zh: ["..."] }
```

---

## 5. 与 UI 技能的协同
1. **UX 决定行为**：定义 `route_path`、`component_roles`、`navigation`、`target_id`。
2. **结构化契约驱动**：必须定义关键组件的预期 DOM 层级（如 `div.data-table-container > table`），为 UI 层的 `dom_shape_valid` 提供交互真值。
3. **UI 决定落地**：选择 CSS 类、HTML 结构，并根据调用方项目结构决定真实文件落点。
4. **接口位预留**：依据 `dev_handoff` 预留数据绑定、状态反馈点与可选 `output_file_hint`。


