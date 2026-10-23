# C06 · Event-Level World Model

> **机制簇**：事件级世界模型 ｜ **家族**：EIM-1.0（Emergent Intelligence Mechanisms）｜ **组件数**：4
>
> 本仓是 EIM-1.0 的**簇级入口**：一个机制簇 + 该簇全部可运行参考实现。
> 单组件仓与旗舰合集见文末「家族」段。

## 费曼三层

**L0 · 这是什么（12 岁能懂）**
让 AI 记住「世界刚才发生了什么」，而不是只看到一张当前快照，所以能预测下一步。

**L1 · 机制本质**
把观测离散成事件 + 谓词状态，用谓词校验状态转移合法性；状态差分成可审计轨迹。

**L2 · 怎么用上**
predicate-state-tracker 维护状态；transition-validator 校验每条边；event-diff 输出变更。

## 30 秒跑起来

```bash
git clone https://github.com/chenhz01/eim-c06-event-level-world-model.git && cd eim-c06-event-level-world-model
python run_all.py        # 跑全簇 4 个组件，逐个 selftest + 输出快照比对
```

单个组件也可独立跑：

```bash
python components/p20-predicate-world-model-runtime/impl.py        # 看 demo 输出
python components/p20-predicate-world-model-runtime/selftest.py    # 断言 + 与 golden_output.txt 比对
```

零第三方依赖，Python 3.9+ 即可。

## 本簇组件

| ID | 组件 | 机制本质 | 目录 |
|---|---|---|---|
| `P20` | predicate-world-model-runtime | 事件驱动状态机：apply(event) 更新谓词集合，check(invariant) 验证不变式。 | `components/p20-predicate-world-model-runtime/` |
| `P21` | event-causality-tracker | 按时间序统计 A→B 共现，生成有向因果候选边。 | `components/p21-event-causality-tracker/` |
| `P22` | state-verification-oracle | 对当前状态批量校验断言集合，返回失败项。 | `components/p22-state-verification-oracle/` |
| `P23` | sim-world-differential-tester | 逐步执行两个 sim，返回首次分歧步与两侧状态。 | `components/p23-sim-world-differential-tester/` |

## 该用 / 不该用 / 常见误用

**该用**
需要多步预测、回放或审计的智能体（运维处置、机器人流程、审批流）。

**不该用**
单步、无状态的问答或抽取任务。

**常见误用（这条最重要）**
谓词写得过宽（永远为真）→ 验证形同虚设。谓词必须配反例测试。

## 这份代码是什么、不是什么

- **是**：可直接运行、带断言与输出快照的最小参考实现。每个 `impl.py` 都能单独跑出 demo，`selftest.py` 会在行为漂移时报错。
- **不是**：生产级库。缺少配置化、并发安全、错误恢复、性能优化。**生产使用请按自己的约束扩展**，不要原样上生产。
- **诚实边界**：本簇解决的是「机制怎么落地」这个问题，不承诺在任何数据分布下都优于基线。基准数据请自测。

## 家族

- **旗舰合集（55 组件）**：https://github.com/chenhz01/emergent-mechanisms
- **单组件仓**：`eim-p01-…` ~ `eim-p55-…`，与 `components/` 内文件一致，任一处修复会双向同步。

## 许可（双许可）

- **代码**：**Apache-2.0**（Apache License 2.0）— 见 [LICENSE](LICENSE)
- **规范/文档**：**CC BY 4.0**（Creative Commons Attribution 4.0 International）— 见 [LICENSE-SPEC](LICENSE-SPEC)

声明符合 EIM-1.0 规范时须署名：

```
EIM-1.0 · C06 · Event-Level World Model © 2026 chenhz01, CC BY 4.0
```

详见 [NOTICE](NOTICE)。
