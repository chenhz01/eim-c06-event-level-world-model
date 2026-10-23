# SPDX-License-Identifier: Apache-2.0
# Copyright 2026 chenhz01 (EIM-1.0)
"""P20 predicate-world-model-runtime — 事件级世界模型

L0: 把世界当成一串'发生了什么事'，每条事都能被检查对不对，而不是一张画。
L1: 事件驱动状态机：apply(event) 更新谓词集合，check(invariant) 验证不变式。
L2: w=PredicateWorldModel(); w.apply('door_open'); w.check('door_open')。
"""

class PredicateWorldModel:
    def __init__(self): self.facts = set()
    def apply(self, event):
        neg = event.startswith("!")
        f = event[1:] if neg else event
        (self.facts.discard if neg else self.facts.add)(f)
        return sorted(self.facts)
    def check(self, invariant): return invariant in self.facts

def demo():
    w = PredicateWorldModel(); w.apply("door_open"); w.apply("light_on")
    print("[P20]", w.apply("!door_open"), "invariant_light_on=", w.check("light_on"))


if __name__ == "__main__":
    demo()
