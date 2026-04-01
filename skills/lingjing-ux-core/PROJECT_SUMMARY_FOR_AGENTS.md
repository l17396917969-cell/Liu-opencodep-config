## 灵境 UX 技能包对话总结（交接用）

> 说明：本文件用于快速交接与接入摘要，便于 AI 工具或协作者快速上手；若需要执行当前正式协议，仍应以 `SKILL.md` 与 `schema/` 为准。

### 一、背景与总目标

- **项目**：`lingjing-ux-core` —— 灵境航空工业智能平台的 **二维 UX 规范技能包**，与 `lingjing-ui-core` UI 规范技能包协同使用。  
- **目标**：
  - 为 AI/非交互同事提供结构化、可执行的交互规范；
  - 通过「模式库 + 场景配置 + 任务流 + 组件交互规范 + Prompt 模板」的方式，让 AI 能稳定产出可交付的 UX 方案；
  - 明确 UX skill 在整体流程中的位置：**产品规划 → UX skill → UI skill → 开发实现**。

---

### 二、整体架构与目录分层（已写入文档）

核心说明在 `SKILL.md` 的 `## 0. 目录结构与分层` 与规划文档的 `4.4` 中。

- **目录与职责**：
  - `modes/`：交互模式卡片（Mode）  
    - 定义在产品场景 × 交互维度下的交互模式、目标、状态与关键交互。
  - `flows/`：任务流骨架（Flow）  
    - 描述从触发到结束的关键步骤序列，可被多个场景复用。
  - `scenes/`：业务场景配置（Scene）  
    - 组合模式与任务流，绑定角色与产品形态，并可关联 `lingjing-ui-core` 示例页面。
  - `component_specs/`：组件交互规范（Component Spec）  
    - 定义通用 UI 组件的行为契约：状态机、交互规则、可配置项、无障碍要求，不包含视觉样式。
  - `schema/`：结构约定层  
    - `ux_output_schema.yml`：标准 UX 输出结构示意（`ux_spec`）。  
    - `component_spec_schema.yml`：组件交互规范结构示意。
  - `examples/`：示例 UX 输出  
    - 具体场景的 `ux_spec_*.yml`，可直接被工具/链路消费。
  - `prompts/`：协作 Prompt 模板  
    - 指导 AI 在不同场景（供应链、军品审批、维修工单）下如何调用技能包。

- **整体流程位置（规划文档 `4.3`）**：
  1. 产品/需求阶段：产生结构化 `design_request`。  
  2. **UX 技能包阶段**：基于 `design_request` → 选 `scene` + `modes` + `flows` → 输出 `ux_spec`（含页面路由、点击流、开发交接信息）。  
  3. UI 技能包阶段（`lingjing-ui-core`）：根据 `ux_spec` 的组件角色、导航关系与技术栈，并结合 `scene_coverage_matrix.yml`，先判定 `Level 1 模板轻调 / Level 2 组件编排 / Level 3 规范扩展`，再生成接入调用方项目的页面层成果（HTML / Vue / React）；其中 B 端顶部栏 + 左侧菜单、网站顶部栏、UE 顶部 HUD 默认属于强一致框架层。  
  4. 开发阶段：依据 `ux_spec` + UI 规范实现真实接口、逻辑状态、权限与非功能约束。



---

### 三、输入/输出协议（给其他工具用的关键约定）

#### 1. 标准输入：`design_request`

- 定义位置：`SKILL.md` 第 1 节「使用方式」中有 YAML 示例。  
- **字段要点**：
  - `id`：本次设计请求标识（可选）。  
  - `business_context_zh`：业务背景与目标。  
  - `product_scene`：`website / b-system / presentation / ai-assistant / ops-console`。  
  - `target_scene_id`：要复用的场景 ID（如 `supply_chain_monitoring`）。  
  - `roles[]`：主要角色（id + name）。  
  - `constraints_zh[]`：实时性、安全、屏幕等约束。  
  - `non_goals_zh[]`：本轮不覆盖的范围。

> 上游工具/同事负责把自然语言需求整理成 `design_request`，再交给 UX skill。

#### 2. 标准输出：`ux_spec`

- 结构示意：`schema/ux_output_schema.yml`。  
- **主要部分**：
  - `design_request`：输入回显。  
  - `scene`：场景 id、说明、目标、启用的 `interaction_modes`、`main_flow`。  
  - `flows[]`：任务流（步骤 id/name/from_mode）。  
  - `pages[]`：
    - `route_path`：页面对应的业务路由路径；多页面/可点击工程场景下应提供，真实文件落点由调用方项目结构决定。  

    - `zones[]`：页面区域与职责。  
    - `component_roles[]`：  
      - `role`：如 `task_board`、`alert_list`；  
      - `lingjing_core_class`：对应 UI 组件类；  
      - `mode_id`：关联模式；  
      - `states[]` 与 `interactions_zh[]`：本场景下的行为；  
      - `action_targets[]`：点击/提交后去哪里（`page / modal / drawer / filter / tab`）。  
  - `navigation`：
    - `entry_page_id`：入口页；  
    - `page_links[]`：页面间跳转关系；  
    - `global_navigation[]`：主导航项（如顶部导航、侧边栏、标签页）。  
  - `dev_handoff`：

    - `api_expectations_zh[]`：接口期望；  
    - `edge_cases_zh[]`：空数据、错误、并发更新等边界；  
    - `tracking_requirements_zh[]`：埋点/审计；  
    - `open_questions_zh[]`：待产品/技术确认的问题。  
  - `meta`：关联 `scenes` / `flows` 文件路径等。

> 多数下游场景通常只需读取 `ux_spec`；若遇到字段扩展、兼容处理或生成歧义，再回查 `SKILL.md`、`schema/` 与示例即可。


---

### 四、已实现的模式 / 场景 / 示例（当前可直接使用）

#### 1. 核心交互模式（`modes/`）

- **`real_time_monitor.yml`**：实时监控模式  
  - 维度：`data_intelligence`，场景：`b-system`。  
  - 状态：`normal / warning / critical`。  
  - 典型应用：供应链战情室、制造运控中心等。

- **`analysis_exploration.yml`**：分析探索模式  
  - 面向自助数据分析：多维筛选、图表/表格联动、保存视图。  
  - UI 映射：`flight-metric-card`、`advanced-data-table`、`chart-card`、`metric-trend`。

- **`exception_handling.yml`**：异常处理流模式  
  - 状态：`detected / triaged / in_progress / resolved / closed`。  
  - 关注从告警 → 异常任务 → 复盘的闭环。

- **`collaboration_task.yml`**：协作任务流模式  
  - 状态：`todo / doing / blocked / done`；支持评论、@、附件、看板拖拽。

- **`approval_workflow.yml`**：多级审批流程模式  
  - 状态：`draft / pending_approval / returned / approved / rejected`。  
  - 适用于军品/关键物资等合规审批场景。

- **`maintenance_workorder.yml`**：设备维修工单模式  
  - 状态：`created / assigned / in_progress / waiting_parts / completed / closed`。  
  - 适用于生产/机场设备维修工单管理。

- **`world_space_ui.yml`**  
  - 为未来 3D 交互 Skill 预留，仅做概念与约束说明，明确当前版本不约束 3D 交互细节。

#### 2. 任务流（`flows/`）

- `monitor_alert_handle.yml`：监控 → 预警 → 分析 → 处置 → 复盘。  
- `procurement_approval.yml`：军品采购：申请发起 → 部门审核 → 合规审查 → 领导审批 → 结果归档。  
- `maintenance_workorder.yml`：设备故障：发现 → 建单 → 分派 → 执行 → 确认与关闭。

#### 3. 场景配置（`scenes/`）

- `supply_chain_monitoring.yml`：供应链监控战情室。  
- `military_procurement_approval.yml`：军品采购审批。  
- `equipment_maintenance_workorder.yml`：设备维修工单管理。

#### 4. 示例 UX 输出（`examples/`）

- **`ux_spec_supply_chain_monitoring.yml`**  
  - 场景：供应链战情室；模式组合：`real_time_monitor` + `exception_handling` + `collaboration_task` + `analysis_exploration`。  
  - 页面：`main_dashboard` + `analysis_view`。  
- **`ux_spec_military_procurement_approval.yml`**  
  - 场景：军品审批；模式：`approval_workflow` + `collaboration_task`。  
  - 页面：`approval_inbox` + `approval_detail`。  
- **`ux_spec_equipment_maintenance_workorder.yml`**  
  - 场景：维修工单；模式：`real_time_monitor` + `maintenance_workorder` + `collaboration_task` + `exception_handling`。  
  - 页面：`workorder_dashboard` + `workorder_detail`。

---

### 五、组件交互规范（`component_specs/`）——试点结果

- **Schema**：`schema/component_spec_schema.yml`  
  - 约束字段：`id / name_zh / summary_zh / states[] / interactions[] / accessibility_zh / config_options[] / meta`。

- **已实现规范**：
  - `component_specs/advanced-data-table.yml`  
    - 定义：高级数据表格组件的行为（`loading / empty / error / normal / selecting`）及排序、过滤、分页、行点击、多选等交互要求。  
    - 配置项：`selection_mode`、`pagination_type`、`empty_state_behavior` 等。  
  - `component_specs/mission-status-board.yml`  
    - 定义：任务/工单看板组件的行为（`loading / empty / normal / dragging`）及拖拽变更状态、卡片点击、列汇总等交互。  
    - 配置项：`allowed_transitions`、`column_order`。

> 这些规范与 `lingjing-ui-core` 的组件通过 `meta.related_lingjing_core_classes` 关联，用于统一行为，不定义视觉。

---

### 六、协作 Prompt 模板（`prompts/`）

- `collab_supply_chain_monitoring.md`  
  - 场景：供应链战情室；引用 `scenes/supply_chain_monitoring.yml` + 相关模式/任务流。  
- `collab_military_procurement_approval.md`  
  - 场景：军品审批；引用 `scenes/military_procurement_approval.yml` + `flows/procurement_approval.yml`。  
- `collab_equipment_maintenance_workorder.md`  
  - 场景：维修工单；引用 `scenes/equipment_maintenance_workorder.yml` + `flows/maintenance_workorder.yml`。

> 这些模板统一约束：仅 2D 界面、聚焦交互行为与信息结构、不输出 CSS，并要求在输出中标明 `scene / mode / flow` 引用。

---

### 七、给后续工具/同事的使用建议

- **如果要新增场景**：  
  1. 补 `scenes/xxx.yml` + 所需 `modes/` + `flows/`。  
  2. 按 `schema/ux_output_schema.yml` 写一份 `examples/ux_spec_xxx.yml`。  
  3. 可选：加一个 `prompts/collab_xxx.md` 协作模板。

- **如果要扩展组件行为**：  
  1. 按 `schema/component_spec_schema.yml` 在 `component_specs/` 中加新组件规范。  
  2. 在已有/新建 `ux_spec` 中通过 `component_roles` 引用，并只写场景特有的行为配置。

- **如果要接入自动化工具**：  
  - 上游请输出结构化 `design_request`；  
  - 让工具调用此技能包生成或读取 `ux_spec_*`；  
  - 下游根据 `ux_spec` 的 `pages + navigation + dev_handoff` 与 UI skill 进行实现和检查；  
  - UI skill 落地时，应先按 `scene_coverage_matrix.yml` 完成 `Level 1 / Level 2 / Level 3` 判定，再选择“模板直用 / 组件编排 / 规范扩展”的实现路径；
  - 若调用方项目已有 Vue / React / 静态 Web 结构，UI skill 应优先对齐现有工程，而不是平行生成孤立 demo；
  - 若页面落在独立项目中，宜先把样式资源放入调用方项目，再检查页面从实际落点访问时样式入口是否成立。



这份 `.md` 可作为「项目简要说明 + 接入摘要」交给其他 AI 工具或同事；若需要落到实际执行，建议再结合这里提到的 `SKILL.md`、`schema/` 与示例文件一起使用。

