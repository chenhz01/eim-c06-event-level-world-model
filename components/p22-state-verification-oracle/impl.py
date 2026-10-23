# SPDX-License-Identifier: Apache-2.0
# Copyright 2026 chenhz01 (EIM-1.0)
"""P22 state-verification-oracle — 事件级世界模型

L0: 运行中随时问'现在世界该是什么样'，答不上就是有 bug。
L1: 对当前状态批量校验断言集合，返回失败项。
L2: verify(model, assertions) → 失败列表。
"""

def verify(model, assertions):
    return [a for a in assertions if not model.check(a)]

def demo():
    class M:
        facts={"a","b"}
        def check(s,x): return x in s.facts
    print("[P22]", verify(M(), ["a","c"]))


if __name__ == "__main__":
    demo()
