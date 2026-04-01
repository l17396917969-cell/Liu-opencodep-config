# LingJing UX Core - 航空工业智能平台 UX 技能包

> **定位**：为 AI 与非交互专业同事提供结构化的交互设计规范，协同 `lingjing-ui-core` UI 技能包，面向航空工业的各类二维产品（后台系统、仪表盘、网站、演示文稿）以及 UE5 Web Overlay / 数字孪生信息叠加层场景。

## 1. 项目结构

本仓库的主要目录与职责如下（详细说明见 `SKILL.md` 与规划文档）：

- `modes/`：交互模式卡片（YAML），描述在特定产品场景和交互维度下的交互模式、目标、状态与关键行为。
- `flows/`：任务流骨架（YAML），用于描述关键任务从触发到完成的步骤序列，可被多个场景复用。
- `scenes/`：业务场景配置（YAML），将多个模式与任务流组合成具体业务场景（如供应链监控战情室、军品采购审批、设备维修工单）。
- `component_specs/`：组件交互规范（YAML），定义通用 UI 组件的行为契约（状态机、交互规则、可配置项），与视觉样式解耦。
- `schema/`：结构约定层，包含 `ux_output_schema.yml`（标准 UX 输出结构）与 `component_spec_schema.yml`（组件规范结构）。
- `examples/`：示例 UX 输出（YAML），例如 `ux_spec_supply_chain_monitoring.yml`，可直接被下游工具消费。
- `prompts/`：AI 提示词模板，指导模型在不同场景下（供应链监控、军品采购审批、设备维修工单）如何使用本 UX 技能包。
- `PROJECT_SUMMARY_FOR_AGENTS.md`：面向 AI 工具/协作者的项目总结与接入说明。

## 2. 使用入口

- **人类 / 团队使用建议**：
  - 阅读 `SKILL.md`：理解整体背景、使用协议与适用场景范围；
  - 阅读 `SKILL.md`：理解本技能包的使用协议、输入 / 输出结构（`design_request` / `ux_spec`）与目录分层；
  - 根据业务选用 `scenes/` 中的场景与 `prompts/` 中的协作模板，与 AI 一起产出交互方案。
- **AI / 工具集成建议**：
  - 上游整理自然语言需求为结构化 `design_request`，然后调用本技能包以场景 + 模式 + 任务流的方式生成 `ux_spec`；
  - 在可写环境中，默认应将完整 `ux_spec` 落盘到调用方项目，而不是只在回复中描述；
  - `ux_spec` 除页面区域与组件职责外，还应包含 `route_path / action_targets / navigation`；其中 `route_path` 表达业务路由，真实文件落点由调用方项目结构决定，可按需补充 `dev_handoff.output_file_hint`；
  - 下游可按“`ux_spec` → `lingjing-ui-core/SKILL.md` + `scene_coverage_matrix.yml` → 调用方项目页面层成果”的顺序衔接工作流；
  - UI 阶段应先完成 `Level 1 / Level 2 / Level 3` 判定：高匹配模板走 Level 1，没有直达模板但组件/模块骨架可承载时走 Level 2，模板与组件都不足时走 Level 3；
  - B 端顶部栏 + 左侧菜单、网站顶部栏、UE 顶部 HUD 属于框架层，UX 在定义页面时应默认这些区域强一致，不建议在 `ux_spec` 中推动重做；
  - 若命中“验证 / 验收 / 复现 / 对标 / 跑通 / 检查技能包”，应先完成 `ux_spec` 落盘，再进入 UI 阶段；
  - 若调用方项目已有 Vue / React / 静态 Web 结构，UI 阶段宜优先对齐现有工程，而不是平行生成独立 demo；
  - 若页面落在独立项目中，更稳妥的做法是先把样式资源落到调用方项目，再生成页面并检查样式引用是否可达；
  - 详细接入约定与现有能力清单见 `PROJECT_SUMMARY_FOR_AGENTS.md`。





## 3. 与 lingjing-ui-core 的关系

- 视觉与组件由 `lingjing-ui-core` 提供（CSS、HTML 组件、页面模板）。
- 交互行为与任务流由本 `lingjing-ux-core` 提供（模式、场景、流程、组件交互规范）。
- 两者通过“组件角色 → 具体 UI 组件类名”的方式绑定，例如：
  - `metric_card -> .flight-metric-card`
  - `alert_panel -> .alert-center-panel`
  - `task_board -> .mission-status-board`
  - `analysis_table -> .advanced-data-table`

## 4. 当前主要内容（v1.0.0）

- 规划与协议：
  - 技能使用协议与分层说明：`SKILL.md`
  - 项目总结与接入说明：`PROJECT_SUMMARY_FOR_AGENTS.md`
- 已沉淀场景与示例：
  - 供应链监控战情室：`scenes/supply_chain_monitoring.yml` + `examples/ux_spec_supply_chain_monitoring.yml`
  - 军品采购审批：`scenes/military_procurement_approval.yml` + `examples/ux_spec_military_procurement_approval.yml`
  - 设备维修工单：`scenes/equipment_maintenance_workorder.yml` + `examples/ux_spec_equipment_maintenance_workorder.yml`
  - 官网落地页（品牌叙事+转化）：`scenes/website_marketing_landing.yml` + `examples/ux_spec_website_marketing_landing.yml`
  - 季度经营汇报（HTML 演示文稿）：`scenes/presentation_quarterly_review.yml` + `examples/ux_spec_presentation_quarterly_review.yml`
  - 运控驾驶舱：`scenes/ops_console_control_tower.yml` + `examples/ux_spec_ops_console_control_tower.yml`
  - AI 助手工作台：`scenes/ai_assistant_workspace.yml` + `examples/ux_spec_ai_assistant_workspace.yml`
- 组件交互规范：
  - 基础业务组件：`component_specs/advanced-data-table.yml`、`component_specs/mission-status-board.yml`
  - 导航与转化：`component_specs/navigation-topbar.yml`、`component_specs/hero-cta.yml`
  - 演示控制：`component_specs/slide-deck-controller.yml`
  - 搜索/通知/抽屉/筛选/图表联动：`component_specs/global-search.yml`、`component_specs/notification-toast.yml`、`component_specs/drawer-filter-bar.yml`、`component_specs/filter-toolbar.yml`、`component_specs/chart-highlight-linking.yml`、`component_specs/command-drawer.yml`
  - AI 风险提示：`component_specs/prompt_ai_guardrail.yml`
- 协作 Prompt 模板：
  - 供应链监控：`prompts/collab_supply_chain_monitoring.md`
  - 军品采购审批：`prompts/collab_military_procurement_approval.md`
  - 设备维修工单：`prompts/collab_equipment_maintenance_workorder.md`
  - 官网落地页：`prompts/collab_website_marketing_landing.md`
  - 季度经营汇报：`prompts/collab_presentation_quarterly_review.md`
  - 运控驾驶舱：`prompts/collab_ops_console_control_tower.md`
  - AI 助手工作台：`prompts/collab_ai_assistant_workspace.md`

更多设计背景与路线图，详见规划文档与上述示例文件。
