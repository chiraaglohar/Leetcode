class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        def bound(need_a: int, cost_a: int, need_b: int, cost_b: int) -> int:
            p_a = min(cost_a, costBoth)  # a takes its full price
            p_b = min(cost_b, costBoth - p_a)  # b gets what's left of the bundle
            return need_a * p_a + need_b * p_b

        return max(bound(need1, cost1, need2, cost2), bound(need2, cost2, need1, cost1))