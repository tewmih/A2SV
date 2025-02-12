class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        right=len(arr)
        result=[]
        while right>1:
            max_index=arr.index(max(arr[:right]))
            if max_index!=right:
                if max_index!=0:
                    result.append(max_index+1)
                    arr[:max_index+1]=reversed(arr[:max_index+1])
                result.append(right)
                arr[:right]=reversed(arr[:right])

            right-=1
        return result