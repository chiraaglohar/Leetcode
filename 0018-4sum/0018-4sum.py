class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        nums.sort()
        res = []
        n = len(nums)

        for i in range(n):

            if i>0 and nums[i]==nums[i-1]:
                continue
            # the first loop

            for j in range(i+1,n):
                if j>i+1 and nums[j]==nums[j-1]:
                    continue
                # The second loop

                l = j+1
                r = n-1
            
                while l<r:
                    # The pointers that move and take care of everything

                    total = nums[i]+nums[j]+nums[l]+nums[r]

                    if target==total:

                        res.append([nums[i],nums[j],nums[l],nums[r]])
                        l+=1
                        r-=1
                        

                        while l<n and nums[l]==nums[l-1]:
                            l+=1

                        while r>=0 and nums[r]==nums[r+1]:
                            r-=1
                    
                    elif total<target:
                        l+=1
                    
                    else:
                        r-=1
    

        return res
