# 协作模板：运控驾驶舱交互设计

> 用途：指导 AI 在 `ops_console_control_tower` 场景下输出结构化 `ux_spec`（禁止只给 Markdown）。

## 提示词示例

> 你是灵境航空工业智能平台的资深 UX 架构师。
> 请基于 `lingjing-ux-core` 与 `lingjing-ui-core`，设计“运控驾驶舱”的交互方案。
>
> 要求：
> 1. 场景：使用 `scenes/ops_console_control_tower.yml`。
> 2. 交互模式：
>    - `ops_multi_source_monitor`（多源态势/告警）
>    - `ops_command_dispatch`（分派/执行/复盘）
> 3. 输出：
>    - 以结构化 `ux_spec` 为主，贴近 `schema/ux_output_schema.yml`；
>    - `pages` 给出区域职责（KPI/态势图/告警/任务板），`component_roles` 写明状态、交互与 `action_targets`（如告警→分派抽屉）；
>    - `dev_handoff` 写清暂停刷新/静音、分派接口、审计要求。
> 4. 约束：
>    - 禁止只输出 Markdown 说明；可先给 ≤5 行摘要，再输出完整 `ux_spec`。
>    - 强调操作安全：分派/批量操作需确认，支持暂停刷新与恢复提示。
