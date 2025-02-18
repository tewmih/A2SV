class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        result = 0
        prefix_remainder={ 0: 1}
        curSum=0

        for num in nums:
            curSum+=num
            result+=prefix_remainder.get(curSum%k,0)
            prefix_remainder[curSum%k] = prefix_remainder.get(curSum%k,0)+1
        return result
