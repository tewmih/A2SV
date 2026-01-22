class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        l,r= 0,0

        result = []

        while r < len(nums):
            if r+1 == len(nums):
                if(l != r):
                    result.append("{}->{}".format(nums[l],nums[r]))
                else:
                    result.append("{}".format(nums[l]))
                r+=1
            elif r + 1 < len(nums)  and nums[r + 1] != nums[r] + 1:
                if l != r:
                    result.append("{}->{}".format(nums[l],nums[r]))
                else:
                    result.append("{}".format(nums[l]))
                r+=1
                l=r
            else:
                r+=1
        return result
            
            