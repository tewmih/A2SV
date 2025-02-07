class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:

        row, col = len(img), len(img[0])
        result = [[0] * col for i in range(row)]

        directions = [(-1, -1),(-1, 0),(-1, 1),(0, -1),(0, 0),(0, 1),(1, -1),(1, 0),(1, 1)]

        for r in range(row):
            for c in range(col):
                total,count=0,0

                for dx,dy in directions:
                    current_row,current_col=r+dy,c+dx
                    if 0<=current_row< row and 0<=current_col<col:
                        total+=img[current_row][current_col]
                        count+=1
                    
                result[r][c]=total//count
        return result
