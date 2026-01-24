class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for i in range(len(nums) - 1):
        #     for  j in range(i + 1, len(nums)):
        #         # check
        #         if(nums[i] + nums[j]) == target:
        #             return [i, j]

        indexed = []
        for i, num in enumerate(nums):
            indexed.append((num, i))
        # sort
        indexed.sort()
        # search
        n = len(nums)

        for i in range(len(nums)):
            l, r = i + 1, n - 1
            compliment = target - indexed[i][0]
            while l <= r:
                mid = l + (r - l)//2
                if indexed[mid][0] < compliment:
                    l = mid  + 1
                elif indexed[mid][0] > compliment:
                    r = mid - 1 
                else:
                    return [indexed[i][1], indexed[mid][1]]
        return []



    

                