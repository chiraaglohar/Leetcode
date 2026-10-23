class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        return (K:=K if (K:=[x for i, x in enumerate(nums) if x!=i]) else [0]) and reduce(operator.and_, K)