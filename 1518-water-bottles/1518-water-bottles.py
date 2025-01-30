class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        sum=numBottles
        remainder=0
        while numBottles>=numExchange:
            sum+=numBottles//numExchange
            numBottles=numBottles//numExchange+numBottles%numExchange
        return sum
            