class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        row=len(mat)
        col=len(mat[0])

        def check(mt):
            ninty=[[0]*col for i in range(row)]
            for i in range(row):
                for j in range(col):
                    ninty[i][j]=mt[(row-j-1)%row][i]
            return ninty
            
        ninty = check(mat)
        one_180=check(ninty)
        two_70=check(one_180)

        # for i in range(row):
        #     for j in range(col):
        #         one_180[i][j]=mat[j][(row-j-1)%row]
        # for i in range(row):
        #     for j in range(col):
        #         two_70[i][j]=mat[(row-j-1)%row][i]
        return (target == mat) or (target == ninty) or (target == one_180) or (target == two_70)
