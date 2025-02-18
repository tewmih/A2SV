class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix=[1]
        suffix = [1]
        product=1
        result=[]

        for pre in nums:
            product*=pre
            prefix.append(product)
        product = 1
        for i in range(len(nums)-1,-1,-1):
            product*=nums[i]
            suffix.append(product)
        suffix.pop()
        prefix.pop()
        # suffix.append(1)
        # suffix.reverse()
        # suffix.append(1)
        n = len(suffix)-1
        print(prefix,suffix)
        for i in range(len(nums)):
            result.append(prefix[i]*suffix[n-i])
        return result

        