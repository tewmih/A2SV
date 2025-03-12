class Solution:
    def getRow(self, i: int) -> List[int]:
        if i == 0:
            return [1]
    
        prev = self.getRow(i - 1)
        temp = [1]
        for j in range(1 , i):
            temp.append(prev[j - 1] + prev[j])

        temp.append(1)
        
        return  temp