# P20 · predicate-world-model-runtime

> 机制簇：**事件级世界模型** ｜ 家族：**EIM-1.0**（55 个涌现智能人工化机制之一）

## 费曼三层

**L0 · 这是什么（12 岁能懂）**
把世界当成一串'发生了什么事'，每条事都能被检查对不对，而不是一张画。

**L1 · 机制本质**
事件驱动状态机：apply(event) 更新谓词集合，check(invariant) 验证不变式。

**L2 · 怎么用上**
w=PredicateWorldModel(); w.apply('door_open'); w.check('door_open')。

## 30 秒跑起来

```bash
python impl.py        # 看 demo 输出
python selftest.py    # 跑自检（含输出快照比对）
```

真实运行输出（本仓发布时快照，`golden_output.txt` 同内容）：

```text
[P20] ['light_on'] invariant_light_on= True
```

## 什么时候该用 / 不该用

| | 内容 |
|---|---|
| **该用** | 状态可枚举、事实会增删改的环境：运维、工作流、机器人、游戏。 |
| **不该用** | 开放语义、无状态定义的开放式对话与创意任务。 |
| **常见误用** | 用 LLM 的自然语言总结当状态——不可判定，无法回答「某事实现在是否成立」。 |

## 在这个家族里

- 组合仓（55 个机制合集）：https://github.com/chenhz01/emergent-mechanisms
- 同簇伙伴：`P21` event-causality-tracker · `P22` state-verification-oracle · `P23` sim-world-differential-tester
- 本仓是 **P20 的独立署名锚**：可单独引用、单独开 issue、单独打星；实现与组合仓
  `components/P20-predicate-world-model-runtime/` 一致，修复会双向同步。

## License

**双许可**：

- **代码**：Apache-2.0 — 见 [LICENSE](LICENSE)
- **文档/规范**：CC BY 4.0 — 见 [LICENSE-SPEC](LICENSE-SPEC)

对外声明「符合 / 兼容 / 通过 EIM-1.0」时须署名：
`EIM-1.0 · P20 · predicate-world-model-runtime © 2026 chenhz01, CC BY 4.0`
未作上述声明者可自由使用、商用、闭源、改名，无需署名。详见 [NOTICE](NOTICE)。
