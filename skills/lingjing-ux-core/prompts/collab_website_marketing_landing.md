# 协作模板：官网落地页交互设计（营销转化）

> 用途：指导 AI 在 `website_marketing_landing` 场景下产出结构化 `ux_spec`，覆盖叙事与转化。

## 提示词示例

> 你是灵境航空工业智能平台的资深 UX 架构师。
> 请基于 `lingjing-ux-core` UX 技能包和 `lingjing-ui-core` UI 技能包，协助我设计一个“官网落地页（品牌叙事+转化）”的交互方案。
>
> 要求：
> 1. 场景：使用 `scenes/website_marketing_landing.yml` 作为基础场景配置。
> 2. 交互模式：
>    - 至少使用 `marketing_storytelling` 和 `cta_conversion`，如需章节导航请指明参数。
> 3. 输出内容：
>    - 以结构化 `ux_spec` 为主，贴近 `schema/ux_output_schema.yml`；
>    - 在 `pages` 中给出区域划分（Hero/价值/佐证/表单），并声明各区域的职责；
>    - 在 `component_roles` 中列出 CTA/导航/表单/佐证卡片的状态、反馈与 `action_targets`（例如主 CTA 滚动到表单锚点）；
>    - 在 `dev_handoff` 中写清表单校验、失败兜底与埋点；
> 4. 约束：
>    - 默认输出 `ux_spec` 结构，不要只给 Markdown 说明；
>    - 动效描述保持轻量，强调加载速度与品牌叙事；
>    - 首屏必须有主 CTA；如有表单，需提供成功/失败反馈与隐私提示。
>
> 请先给出不超过 5 行的中文摘要，然后输出完整 `ux_spec`。字段中的 `description_zh` / `responsibility_zh` / `interactions_zh` 可标注模式引用（如 `[mode: marketing_storytelling]`）。

---

可根据实际产品添加价格/FAQ/对比等区块，但仍需保持 `ux_spec` 结构化输出。