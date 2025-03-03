class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        perimeter = 0
        nums.sort(reverse = True)

        for l in range(len(nums)-2):
            if nums[l]<nums[l+1]+nums[l+2]:
                return nums[l] + nums[l+1] + nums[l+2]
        return perimeter