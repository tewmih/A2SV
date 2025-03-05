class Solution:
    def minMoves(self, target: int, mx: int) -> int:
        
        moves = 0
        while target > 1:

            if target % 2 == 0 :

                if mx > 0:
                    mx -= 1
                    target //= 2
                    moves  += 1
                else:
                    moves  += (target - 1)
                    return moves
            else:
                target -= 1
                moves += 1


        return moves