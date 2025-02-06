import math
class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        even_sum=sum(num for num in nums if num%2==0)
        result=[]
        for val,index in queries:
            old=nums[index]
            nums[index]+=val
            if old%2==0:
                even_sum-=old
            if nums[index]%2==0:
                even_sum+=nums[index]
            result.append(even_sum)

        return result