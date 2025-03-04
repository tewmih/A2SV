class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        s = list(s)
        ones = s.count('1')
        zeros = s.count('0')
        res = ['0']*(len(s))
        for i in range(ones-1):
            res[i] = '1'
        res[-1] = '1'
        return ''.join(res)
        