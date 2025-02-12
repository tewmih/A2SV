class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        chemistry=-1
        skill.sort()
        left = 0
        right=len(skill)-1
        result=[]
        while left<right:
            result.extend([skill[left],skill[right]])
            left+=1
            right-=1
        print(result)
        check=result[0]+result[1]
        print(check)
        total=0
        l=0
        r=1
        while r<len(result):
            if result[l]+result[r]!=check:
                return -1
            total+=(result[l]*result[r])
            l+=2
            r+=2
        return total
        