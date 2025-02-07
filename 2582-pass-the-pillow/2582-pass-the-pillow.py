class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        cycle = time // (n - 1)  
        remainder = time % (n - 1)  

        if cycle % 2 == 0:
            return 1 + remainder 
        else:
            return n - remainder  
