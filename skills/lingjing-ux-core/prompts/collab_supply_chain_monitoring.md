# 协作模板：供应链监控战情室交互设计

> 用途：指导 AI 与设计者协作，在 `supply_chain_monitoring` 场景下产出一份结构化的交互方案。

## 提示词示例（供人类直接粘贴给 AI）

> 你现在是灵境航空工业智能平台的资深UX架构师。
> 请基于 `lingjing-ux-core` UX技能包和 `lingjing-ui-core` UI技能包，协助我设计一个“供应链监控战情室”的交互方案。
>
> 要求：
> 1. 场景：使用 `scenes/supply_chain_monitoring.yml` 作为基础场景配置。
> 2. 交互模式：
>    - 至少使用 `real_time_monitor` 模式，并根据需要组合其他模式（如异常处理、协作任务等，如果已存在）。
> 3. 输出内容：
>    - 请将方案组织为以 `ux_spec` 为主的结构化结果，尽量贴近 `schema/ux_output_schema.yml`；
>    - 在 `scene` 中说明目标、主要角色与约束条件；
>    - 在 `flows` 中表达“监控 → 预警 → 分析 → 模拟 → 执行”这类关键任务流及每一步的入口与结果；
>    - 在 `pages` 中描述页面蓝图，并通过 `zones` 说明顶部 KPI 区 / 主告警区 / 详情区等区域的交互职责；
>    - 在 `component_roles` 中列出关键组件及其状态、反馈、错误处理和动作目标；
>    - 在 `dev_handoff` 中补充权限、审计、合规等交接要求。
> 4. 约束：
>    - 本次方案仅针对二维平面仪表盘界面，不需要设计三维场景中的摄像机/视角交互。
>    - 请避免输出具体 CSS 细节，专注于交互行为与信息结构。
>
> 请以结构化 `ux_spec` 作为主输出；如需帮助人阅读，可先给出不超过 5 行的简短摘要，再输出完整 `ux_spec`。可在相关 `description_zh` / `responsibility_zh` / `interactions_zh` 字段中标明模式/场景配置引用（例如：`[mode: real_time_monitor]`、`[scene: supply_chain_monitoring]`）。


---

后续可以根据项目反馈，补充更多协作模板（例如：运控驾驶舱、维修工单协作、军品采购审批等）。