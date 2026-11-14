class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        n = len(nums)
        best = float('inf')

        for length in range(l, r + 1):
            for i in range(n - length + 1):
                s = sum(nums[i:i + length])
                if 0 < s < best:
                    best = s

        return -1 if best == float('inf') else best