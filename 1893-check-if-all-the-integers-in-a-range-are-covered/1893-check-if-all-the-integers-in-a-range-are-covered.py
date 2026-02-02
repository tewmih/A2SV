class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        new_set = set()
        for num in ranges:
            new_set.update(range(num[0], num[1]+1))
        num = range(left, right + 1)

        for i in range(len(num)):
            if(num[i]) not in new_set:
                return False

        return True

