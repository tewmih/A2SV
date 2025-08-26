class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        sum = 0

        result = set()
        for i in range(len(nums)):
            next = i + 1
            right = len(nums) - 1
            while next < right:
                sum = nums[i] + nums[next] + nums[right]
                if sum < 0:
                    next = next + 1
                elif sum > 0:
                    right = right - 1
                else:
                    result.add((nums[i], nums[next], nums[right]))
                    next += 1
                    right -= 1
        return [list(triplet) for triplet in result]
