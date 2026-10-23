# P23 · sim-world-differential-tester

> 机制簇：**事件级世界模型** ｜ 家族：**EIM-1.0**（55 个涌现智能人工化机制之一）

## 费曼三层

**L0 · 这是什么（12 岁能懂）**
让两个模拟器跑同一串操作，第一个不同的地方就是 bug 所在。

**L1 · 机制本质**
逐步执行两个 sim，返回首次分歧步与两侧状态。

**L2 · 怎么用上**
diff(simA, simB, actions) → (step, a, b) 或 None。

## 30 秒跑起来

```bash
python impl.py        # 看 demo 输出
python selftest.py    # 跑自检（含输出快照比对）
```

真实运行输出（本仓发布时快照，`golden_output.txt` 同内容）：

```text
[P23] (2, 6, 9)
```

## 什么时候该用 / 不该用

| | 内容 |
|---|---|
| **该用** | 状态可枚举、事实会增删改的环境：运维、工作流、机器人、游戏。 |
| **不该用** | 开放语义、无状态定义的开放式对话与创意任务。 |
| **常见误用** | 用 LLM 的自然语言总结当状态——不可判定，无法回答「某事实现在是否成立」。 |

## 在这个家族里

- 组合仓（55 个机制合集）：https://github.com/chenhz01/emergent-mechanisms
- 同簇伙伴：`P20` predicate-world-model-runtime · `P21` event-causality-tracker · `P22` state-verification-oracle
- 本仓是 **P23 的独立署名锚**：可单独引用、单独开 issue、单独打星；实现与组合仓
  `components/P23-sim-world-differential-tester/` 一致，修复会双向同步。

## License

**双许可**：

- **代码**：Apache-2.0 — 见 [LICENSE](LICENSE)
- **文档/规范**：CC BY 4.0 — 见 [LICENSE-SPEC](LICENSE-SPEC)

对外声明「符合 / 兼容 / 通过 EIM-1.0」时须署名：
`EIM-1.0 · P23 · sim-world-differential-tester © 2026 chenhz01, CC BY 4.0`
未作上述声明者可自由使用、商用、闭源、改名，无需署名。详见 [NOTICE](NOTICE)。
