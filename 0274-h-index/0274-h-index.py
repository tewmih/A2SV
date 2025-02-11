class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        h=0
        for i in range(len(citations)):
            if len(citations)-i<=citations[i]:
                h=max(h,len(citations)-i)
        return h