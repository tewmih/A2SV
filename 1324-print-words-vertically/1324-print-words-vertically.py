class Solution(object):
    def printVertically(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        s=s.split() 

        max_len= max(len(item) for item in s)
        result=[""]*max_len
        for i in range(max_len):
            for word in s:
                if i<len(word):
                    result[i]+=word[i]
                else:
                    result[i]+=" "
            result[i]=result[i].rstrip()
        return result