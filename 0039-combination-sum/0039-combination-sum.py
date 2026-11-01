
class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []

        def makeCombination(idx, comb, total):
            if total == target:
                res.append(comb.copy())
                return

            if total > target or idx >= len(candidates):
                return

            # Include the current candidate
            comb.append(candidates[idx])
            makeCombination(idx, comb, total + candidates[idx])

            # Backtrack
            comb.pop()

            # Skip the current candidate
            makeCombination(idx + 1, comb, total)

        makeCombination(0, [], 0)
        return res