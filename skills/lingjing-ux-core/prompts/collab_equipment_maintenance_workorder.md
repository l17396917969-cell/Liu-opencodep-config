# 协作模板：设备维修工单交互设计

> 用途：指导 AI 与设计者协作，在 `equipment_maintenance_workorder` 场景下产出一份结构化的交互方案。

## 提示词示例（供人类直接粘贴给 AI）

> 你现在是灵境航空工业智能平台的资深UX架构师。
> 请基于 `lingjing-ux-core` UX技能包和 `lingjing-ui-core` UI技能包，协助我设计一个“设备维修工单管理系统”的交互方案。
>
> 要求：
> 1. 场景：使用 `scenes/equipment_maintenance_workorder.yml` 作为基础场景配置。
> 2. 交互模式：
>    - 至少使用 `maintenance_workorder` 模式，并结合 `real_time_monitor`、`collaboration_task`、`exception_handling` 等模式说明联动关系。
> 3. 输出内容：
>    - 请将方案组织为以 `ux_spec` 为主的结构化结果，尽量贴近 `schema/ux_output_schema.yml`；
>    - 在 `scene` 中说明目标、主要角色（维修计划员/维修技师/运行主管）与约束条件；
>    - 在 `flows` 中表达基于 `flows/maintenance_workorder.yml` 的“故障发现 → 创建工单 → 分派 → 执行 → 确认与关闭”关键任务流；
>    - 在 `pages` 中至少描述“工单看板页”和“工单详情页”，并通过 `zones` 说明筛选区 / 看板区 / 基本信息区 / 操作区 / 历史区的交互职责；
>    - 在 `component_roles` 中列出关键组件（如 `mission-status-board`、`content-card`、`activity-timeline`）及其状态、反馈、错误处理和动作目标；
>    - 在 `dev_handoff` 中补充状态变更记录、关键操作确认、防止误关工单等要求。
> 4. 约束：
>    - 本次方案仅针对二维后台系统界面，不需要设计三维场景中的交互细节。
>    - 请避免输出具体 CSS 细节，专注于交互行为与信息结构。
>
> 请以结构化 `ux_spec` 作为主输出；如需帮助人阅读，可先给出不超过 5 行的简短摘要，再输出完整 `ux_spec`。可在相关 `description_zh` / `responsibility_zh` / `interactions_zh` 字段中标明模式/场景配置引用（例如：`[scene: equipment_maintenance_workorder]`、`[mode: maintenance_workorder]`、`[flow: maintenance_workorder]`）。

