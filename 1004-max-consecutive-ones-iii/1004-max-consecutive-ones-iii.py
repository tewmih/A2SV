class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        count=0
        longest=float('-inf')
        left=0
        
        for i in range(len(nums)):
            if nums[i]==0:
                count+=1

            while count>k:
                if nums[left]==0:
                    count-=1
                left+=1
            
            longest=max(longest,(i-left+1))
        return longest
        
            

