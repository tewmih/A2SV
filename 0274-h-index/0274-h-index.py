class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        h=0
        for i in range(len(citations)):
            h=max(h,min(len(citations)-i, citations[i]))
        return h