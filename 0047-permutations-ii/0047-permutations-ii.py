class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        result = []
        def permute(i):
            if i == len(nums):
                result.append(nums.copy())
                return
            seen = set()
            for j in range(i, len(nums)):
                if nums[j] not in seen:
                    seen.add(nums[j])
                    nums[i], nums[j] = nums[j], nums[i]
                    permute(i+1)
                    nums[i], nums[j] = nums[j], nums[i]           

        permute(0)
        return result 