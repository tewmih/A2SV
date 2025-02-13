class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window=0
        left=0
        max_val=float("-inf")

        for i in range(len(nums)):
            if i<k:
                window+=nums[i]
            else:
                window=window+nums[i]-nums[left]
                left+=1
            if i>=k-1:
                max_window=window
                max_val=max(max_window,max_val)
        return max_val/k
        