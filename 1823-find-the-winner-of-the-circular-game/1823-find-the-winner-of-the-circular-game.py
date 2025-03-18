class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        k = k -1
        arr = list(range(1,n+1))
        
        def circle(index):
            nonlocal arr
            if len(arr) == 1:
                return arr[0]

            index = (k + index)%len(arr)

            arr.pop(index)
            return circle(index)
        return circle(0)