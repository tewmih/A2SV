class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        counter=0
        h=0
        print(citations)
        for i in range(len(citations)):
            if len(citations)-i<=citations[i]:
                h=max(h,len(citations)-i)
        return h

