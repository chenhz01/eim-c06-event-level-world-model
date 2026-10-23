# SPDX-License-Identifier: Apache-2.0
# Copyright 2026 chenhz01 (EIM-1.0)
"""P23 sim-world-differential-tester — 事件级世界模型

L0: 让两个模拟器跑同一串操作，第一个不同的地方就是 bug 所在。
L1: 逐步执行两个 sim，返回首次分歧步与两侧状态。
L2: diff(simA, simB, actions) → (step, a, b) 或 None。
"""

def diff(simA, simB, actions):
    for i, a in enumerate(actions):
        sa, sb = simA(a), simB(a)
        if sa != sb: return i, sa, sb
    return None

def demo():
    A = lambda a: a * 2
    B = lambda a: a * 2 if a < 3 else a * 3
    print("[P23]", diff(A, B, [1,2,3,4]))


if __name__ == "__main__":
    demo()
