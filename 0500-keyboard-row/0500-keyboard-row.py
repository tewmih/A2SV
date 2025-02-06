class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        result=[]
        row1=set('qwertyuiop')
        row2=set('asdfghjkl')
        row3=set('zxcvbnm')
        for word in words:
            temp_set=set(word.lower())
            if temp_set.issubset(row1) or temp_set.issubset(row2) or temp_set.issubset(row3):
                result.append(word)
            
        return result
