class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach =   float('-inf')
        if len(nums)==1:
            return True

        for i in range(len(nums)):
            # print(i,max_reach)
            max_reach = max( max_reach , i + nums[i])
            if max_reach <= i:
                return False
            if max_reach >= len(nums)-1:
                return True
        else:
            return True

