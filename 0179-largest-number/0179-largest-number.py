class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums= list(map(str,nums))#to convert to string
        nums.sort(key=lambda x:x*9,reverse=True)

        if nums[0]=='0':
            return "0"
        return "".join(nums)
      