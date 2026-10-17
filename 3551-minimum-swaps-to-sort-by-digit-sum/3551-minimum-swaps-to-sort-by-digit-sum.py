class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        def digit_sum(x: int) -> int:
            s = 0
            while x > 0:
                s += x % 10
                x //= 10
            return s

        n = len(nums)
        order = sorted(range(n), key=lambda i: (digit_sum(nums[i]), nums[i]))

        vis = [False] * n
        swaps = 0
        for i in range(n):
            if vis[i] or order[i] == i:
                continue
            j, length = i, 0
            while not vis[j]:
                vis[j] = True
                j = order[j]
                length += 1
            swaps += length - 1
        return swaps