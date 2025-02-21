class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        res = [0]*(len(nums)+1)

        for request in requests:
            res[request[0]] += 1
            res[request[1]+1] -= 1
        cur_sum = 0
        prefix = []
        for i in range(len(res)):
            cur_sum += res[i]
            prefix.append(cur_sum)
        nums.sort(reverse = True)
        prefix.sort(reverse = True)        
        final = 0
        for i in range(len(nums)):
            final+=(nums[i]*prefix[i])
        return(final)%(10**9 + 7)