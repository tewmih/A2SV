class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        s = list(s)
        res = [0]*(len(s)+1)

        for shift in shifts:
            if shift[2] == 0:
                res[shift[0]] -=1
                res[shift[1]+1] +=1
            else:
                res[shift[0]] +=1
                res[shift[1] + 1] -=1
        cur_sum = 0
        
        for i in range(len(s)):
            cur_sum+=res[i]
            res[i] = cur_sum
            if res[i] <0:
                s[i] = chr(((ord(s[i]) - ord('a') +res[i]+ 26) % 26) + ord('a'))
            else:
                s[i] = chr(((ord(s[i]) - ord('a') +res[i]) % 26) + ord('a'))
        
        return("".join(s))