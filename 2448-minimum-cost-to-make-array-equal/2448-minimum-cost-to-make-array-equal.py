class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        combo = sorted(zip(nums,cost))
        n = len(combo)
        cost_sum = 0
        prefix =[0]*n
        prev_sum = 0

        for i  in range(n):
            if i>0:
                diff = abs(combo[i][0] - combo[i-1][0])
                prefix[i] = prev_sum + diff*cost_sum
                prev_sum = prefix[i]
            cost_sum += combo[i][1]
        suffix = [0]*n
        cost_sum = 0
        prev_sum = 0

        for i in range(n-1,-1,-1):
            if i < len(combo)-1:
                diff = abs(combo[i][0] - combo[i+1][0])
                suffix[i] = prev_sum + diff*cost_sum
                prev_sum = suffix[i]
            cost_sum += combo[i][1]
        total_cost = [prefix[i] + suffix[i] for i in range(n)]
        return min(total_cost)
