class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        l = len(nums)
        big_num = l + 1
        missing_num = 1
        for i in range(l):
            if nums[i] <= 0:
                nums[i] = big_num
        for num in nums:
            idx = abs(num) - 1
            if idx < l:
                nums[idx] = abs(nums[idx]) * -1
        for num in nums:
            if num > 0:
                return missing_num
            missing_num += 1
        return missing_num