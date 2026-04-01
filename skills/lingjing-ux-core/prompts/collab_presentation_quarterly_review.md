# 协作模板：季度经营汇报（HTML 演示文稿）

> 用途：指导 AI 在 `presentation_quarterly_review` 场景下生成结构化 `ux_spec`，强调章节导航、数据亮点与互动。

## 提示词示例

> 你是灵境航空工业智能平台的资深 UX 架构师。
> 请基于 `lingjing-ux-core` UX 技能包和 `lingjing-ui-core` UI 技能包，设计“季度经营汇报”HTML 演示文稿的交互方案。
>
> 要求：
> 1. 场景：使用 `scenes/presentation_quarterly_review.yml`。
> 2. 交互模式：
>    - 使用 `deck_navigation` 处理章节导航/翻页；
>    - 使用 `audience_engagement` 处理 Q&A / 投票。
> 3. 输出内容：
>    - 以结构化 `ux_spec` 为主，贴近 `schema/ux_output_schema.yml`；
>    - `pages` 需覆盖议程、指标、决策、Q&A 等关键页，给出 `route_path` 与区域职责；
>    - `component_roles` 要包含幻灯控制器、章节导航、Q&A 组件的状态、交互与 `action_targets`；
>    - `navigation` 写清入口页与页面跳转关系；
>    - `dev_handoff` 写清离线/备注隔离、Q&A 数据接口要求。
> 4. 约束：
>    - 必须输出 `ux_spec` 结构，不要只给 Markdown 说明；
>    - 动效保持克制，可提供无动效选项；
>    - 备注/演讲者视图不应暴露给听众。
>
> 请先给出不超过 5 行的中文摘要，再输出完整 `ux_spec`。字段中的 `description_zh` / `responsibility_zh` / `interactions_zh` 可标注模式引用（如 `[mode: deck_navigation]`）。

---

如有特殊议程（路演/培训），可调整章节与 Q&A 策略，但仍需遵循 `ux_spec` 结构化输出。