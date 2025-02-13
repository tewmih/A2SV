class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        nums.sort()
        left=0
        right=len(nums)-1
        total=0
        result=float('inf')
        min_val=float('inf')

        for i in range(len(nums)):
            left=i+1
            while left<right and right<len(nums):
                total=nums[i]+nums[left]+nums[right]
                dif=abs(total-target)
                if dif<min_val:
                    min_val=dif
                    result=total

                if total>target:
                    while left<right and nums[right]==nums[right-1]:
                        right-=1
                    right -=1
                elif total<target:
                    while left<right and nums[left]==nums[left+1]:
                        left+=1
                    left+=1
                else:
                    return total
        return result
