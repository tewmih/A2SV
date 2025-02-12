class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        count=0
        val_sum=0
        for i in range(len(costs)):
            val_sum+=costs[i]
            if val_sum<=coins:
                count+=1
        return count