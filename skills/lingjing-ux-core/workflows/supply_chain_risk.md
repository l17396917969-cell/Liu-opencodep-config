# 供应链风险处理结构化流程图 (Supply Chain Risk Workflow)

**场景定位**：针对航空供应链中的核心物料断供或延迟，定义的标准应急响应与处理流程。

---

## Mermaid 流程图 (机器可读)

```mermaid
graph TD
    %% 开始与发现
    Start((发现风险事件)) --> Detect{异常自动分类}
    
    %% 异常分类 (维度 1)
    Detect -- 供应商停工 --> Critical[Critical: 严重中断]
    Detect -- 物流延迟 < 48h --> Warning[Warning: 预警关注]
    Detect -- 质量轻微波动 --> Info[Info: 低风险记录]

    %% 处理逻辑 (模式组合)
    Critical --> Triage[建立异常处理工单: Triage]
    Triage --> MultiApproval[多级审批: 并行会签]
    MultiApproval -- 通过 --> ReRoute[紧急物流重排/换供应商]
    MultiApproval -- 驳回 --> ReEvaluate[重新评估风险影响]
    
    Warning --> Notify[自动通知供应计划员]
    Notify --> Monitor[持续监控: real_time_monitor]
    Monitor --> CheckResolved{风险是否解除?}
    CheckResolved -- 是 --> Close[流程关闭: Closed]
    CheckResolved -- 否 --> Critical

    %% 合规卡点 (维度 3)
    ReRoute --> Audit[审计追踪记录: audit_trail]
    Audit --> FAA_Check{FAA/EASA 合规检查}
    FAA_Check -- 不通过 --> Correct[限期整改并重提]
    FAA_Check -- 通过 --> Execute[执行应急采购方案]

    %% 结束与复盘
    Execute --> Close
    Close --> Report[生成 AI 复盘建议]
    Report --> End((流程结束))

    %% 样式修饰 (UI 映射)
    style Critical fill:#ff4d4f,stroke:#fff,stroke-width:2px,color:#fff
    style Warning fill:#faad14,stroke:#fff,stroke-width:2px,color:#fff
    style MultiApproval stroke-dasharray: 5 5
    style Audit fill:#1890ff,stroke:#fff,color:#fff
```

---

## 关键节点定义 (Key Decision Nodes)

### 1. 风险分类 (Detect & Triage)
- **触发条件**：基于 `real_time_monitor` 模式中的 `critical` 状态。
- **决策规则**：若受影响物料涉及“关键飞行安全件”，默认升格为 `Critical` 等级。

### 2. 多级审批 (Multi-Level Approval)
- **合规卡点**：航空制造合同变更必须由质量部 (Quality) 与 合规部 (Compliance) 同时并行会签，不可由采购部单方决定。
- **关联模式**：`patterns/multi_level_approval.yml`。

### 3. FAA/EASA 合规检查 (Compliance Check)
- **硬性约束**：所有更换供应商的操作必须符合现行适航指令 (AD) 库。若新供应商不具备对应资质，流程强制阻断。

### 4. 异常处理记录 (Audit & Report)
- **落地要求**：处理过程中的所有对话、决策附件、时间点必须写入 `ux_spec.dev_handoff.tracking_requirements_zh`，确保事故后可一键追溯。

---

## AI 调用建议 (AI Usage)

- **查询**：当 AI 被问及“如何处理供应商突然停产”时，应提取本流程中的 `Critical -> Triage -> MultiApproval` 路径进行建议。
- **自动化**：当环境支持时，AI 可依据本 Markdown 自动解析流程逻辑，并为用户生成对应的 `ux_spec` 任务流部分。
