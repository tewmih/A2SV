class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []
        
        result=[]
        while matrix:
            result+=matrix.pop(0)
            if matrix and matrix[0]:
                matrix=list(zip(*matrix))[::-1]
        return result