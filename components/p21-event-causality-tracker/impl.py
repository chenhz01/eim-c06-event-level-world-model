# SPDX-License-Identifier: Apache-2.0
# Copyright 2026 chenhz01 (EIM-1.0)
"""P21 event-causality-tracker — 事件级世界模型

L0: 看日志里谁总在谁之前发生，猜出'因为所以'。
L1: 按时间序统计 A→B 共现，生成有向因果候选边。
L2: track(logs) 返回边列表 (a,b,score)。
"""

def track(logs, min_support=1):
    from collections import Counter
    c = Counter()
    for seq in logs:
        for i in range(len(seq)-1):
            c[(seq[i], seq[i+1])] += 1
    return [(a,b,n) for (a,b),n in c.items() if n >= min_support]

def demo():
    print("[P21]", track([["login","open","buy"],["login","open","exit"],["open","buy"]]))


if __name__ == "__main__":
    demo()
