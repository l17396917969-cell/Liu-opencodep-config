# 协作模板：AI 助手工作台

> 用途：指导 AI 在 `ai_assistant_workspace` 场景下生成结构化 `ux_spec`（禁止只给 Markdown）。

## 提示词示例

> 你是灵境航空工业智能平台的资深 UX 架构师。
> 请基于 `lingjing-ux-core` 与 `lingjing-ui-core`，设计“AI 助手工作台”的交互方案。
>
> 要求：
> 1. 场景：使用 `scenes/ai_assistant_workspace.yml`。
> 2. 交互模式：
>    - `assistant_multi_turn_planning`（澄清/规划）
>    - `assistant_tool_execution`（工具执行）
> 3. 输出：
>    - 主输出为结构化 `ux_spec`，贴近 `schema/ux_output_schema.yml`；
>    - `pages` 覆盖对话、计划、执行日志、结果区，写明 `route_path`、`zones`、`component_roles` 与 `action_targets`；
>    - `dev_handoff` 写清日志审计、高风险确认、失败重试策略。
> 4. 约束：
>    - 禁止只输出 Markdown 说明；如需摘要，≤5 行附在前。"
>    - 保留对话与执行日志上下文，不得因翻页丢失。"
