# 协作模板：军品采购审批交互设计

> 用途：指导 AI 与设计者协作，在 `military_procurement_approval` 场景下产出一份结构化的交互方案。

## 提示词示例（供人类直接粘贴给 AI）

> 你现在是灵境航空工业智能平台的资深UX架构师。
> 请基于 `lingjing-ux-core` UX技能包和 `lingjing-ui-core` UI技能包，协助我设计一个“军品采购审批系统”的交互方案。
>
> 要求：
> 1. 场景：使用 `scenes/military_procurement_approval.yml` 作为基础场景配置。
> 2. 交互模式：
>    - 至少使用 `approval_workflow` 模式，并根据需要组合 `collaboration_task` 等其他模式。
> 3. 输出内容：
>    - 请将方案组织为以 `ux_spec` 为主的结构化结果，尽量贴近 `schema/ux_output_schema.yml`；
>    - 在 `scene` 中说明目标、主要角色（申请人/部门负责人/合规/领导）与约束条件；
>    - 在 `flows` 中表达基于 `flows/procurement_approval.yml` 的“申请发起 → 部门审核 → 合规审查 → 领导审批 → 结果归档”关键任务流；
>    - 在 `pages` 中至少描述“审批待办列表页”和“审批详情页”，并通过 `zones` 说明筛选区 / 列表区 / 详情区 / 历史区的交互职责；
>    - 在 `component_roles` 中列出关键组件（如 `advanced-data-table`、`activity-timeline`、`form-layout`）及其状态、反馈、错误处理和动作目标；
>    - 在 `dev_handoff` 中补充权限控制、审计记录、意见不可篡改等要求。
> 4. 约束：
>    - 本次方案仅针对二维后台审批系统界面，不需要设计三维场景中的交互。
>    - 请避免输出具体 CSS 细节，专注于交互行为、信息结构与审批制度相关的 UX 约束。
> 
> 请以结构化 `ux_spec` 作为主输出；如需帮助人阅读，可先给出不超过 5 行的简短摘要，再输出完整 `ux_spec`。可在相关 `description_zh` / `responsibility_zh` / `interactions_zh` 字段中标明模式/场景配置引用（例如：`[scene: military_procurement_approval]`、`[mode: approval_workflow]`、`[flow: procurement_approval]`）。

