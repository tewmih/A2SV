class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        leng = 2 ** (n - 1)
        
        if leng == 1:
            return 0
        print(n, k, leng)

        if k > leng // 2:
            val = self.kthGrammar(n - 1, k - (leng / 2))
            return abs(val - 1)
        else:
            return self.kthGrammar(n - 1, k)
