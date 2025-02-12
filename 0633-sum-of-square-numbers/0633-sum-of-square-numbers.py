class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        possible_squares=int(sqrt(c))
        squares=[i*i for i in range(possible_squares+1)]
        left=0
        right=len(squares)-1
        while left<=right:
            product=squares[left]+squares[right]
            if product<c:
                left+=1
            elif product>c:
                right-=1
            elif product==c:
                return True
            
        return False