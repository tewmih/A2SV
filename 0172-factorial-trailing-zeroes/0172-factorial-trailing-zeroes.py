class Solution:
    def five_produces(self,n:int) ->int:
        if n < 5:
            return 0
        return (n//5 + self.five_produces(n//5))
    def trailingZeroes(self, n: int) -> int:
        return self.five_produces(n)