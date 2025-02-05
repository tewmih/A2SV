class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        right=len(nums)-1
        for i in range(len(nums)-2,-1,-1):
            if nums[i]==nums[i+1]:
                nums[right]=nums[i]
                right=right-1
        return nums[right+1:]