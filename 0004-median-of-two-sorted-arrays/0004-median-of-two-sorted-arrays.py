class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        merged = nums1 + nums2
        merged.sort()
        total = len(merged)
        if total % 2 == 1:
            return float(merged[total // 2])
        else:
            middle1 = merged[total // 2 - 1]
            middle2 = merged[total // 2]
            return (float(middle1) + float(middle2)) / 2.0