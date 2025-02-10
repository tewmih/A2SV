class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        my_dict= {}
        for i in range(len(heights)):
            my_dict[heights[i]]=names[i]
        for i in range(len(heights)-1):
            if(heights[i+1]>heights[i]):
                heights[i],heights[i+1]=heights[i+1],heights[i]
                names[i],names[i+1]=names[i+1],names[i]
        return names


