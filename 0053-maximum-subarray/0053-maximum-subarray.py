class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxim=float('-inf')
        prevSum= nums[0]

        curSum = 0
        for num in nums:
            curSum+=num
            if prevSum < 0:
                curSum= num
            maxim = max(maxim, curSum)
            prevSum=curSum
            

        return maxim
