class Solution:
    def searchInsert(self, nums, target):

        start = 0
        end = len(nums) - 1
        mid = 0

        while start <= end:

            mid = start + (end - start) // 2

            if nums[mid] == target:
                return mid

            elif nums[mid] < target:
                start = mid + 1

            else:
                end = mid - 1

        return mid + 1 if target > nums[mid] else mid