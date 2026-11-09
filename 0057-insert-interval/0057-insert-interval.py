class Solution:
    def insert(self, nums: list[list[int]], newnum: list[int]) -> list[list[int]]:
        ans = []
        for i in range(len(nums)):
            if newnum[1] < nums[i][0]:
                ans.append(newnum)
                return ans + nums[i:]
            elif newnum[0] > nums[i][1]:
                ans.append(nums[i])
            else:
                newnum = [min(newnum[0], nums[i][0]), max(newnum[1], nums[i][1])]
        ans.append(newnum)
        return ans