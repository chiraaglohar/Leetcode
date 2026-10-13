class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        n = len(nums)
        h = n // 2

        nums = sorted(abs(x) for x in nums)

        ans = 0
        for i in range(n):
            ans += (-1 if i < h else 1) * nums[i] * nums[i]

        return ans