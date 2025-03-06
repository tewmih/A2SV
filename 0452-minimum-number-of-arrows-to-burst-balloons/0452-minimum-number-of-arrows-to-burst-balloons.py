class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:

        points.sort(key = lambda x:(x[1]))
        left = 0
        count = 0
        _min_end = float('inf')
        while left < len(points):
            hold = points[left][1]
            while  left < len(points)-1 and hold >= points[left+1][0]:
                # print(hold, points[left+1][0])
                _min_end = min(_min_end,points[left][1])
                if _min_end < points[left][0]:
                    count += 1
                left += 1
            # if left+1 < len(points):
            #     print(hold, points[left+1][0])
            count += 1
            left+=1
            if left + 1 < len(points):
                _min_end = points[left][1]
        return(count)