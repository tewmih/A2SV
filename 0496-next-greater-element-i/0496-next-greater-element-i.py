class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        monotonic = [-1]*len(nums2)

        for i in range(len(nums2)):
            while stack and nums2[stack[-1]] < nums2[i]:
                index = stack.pop()
                monotonic[index] = nums2[i]
                # print('monotonic',monotonic, nums2[index])
            stack.append(i)
            # print('sta',stack, nums2[i])
        _map = dict(zip(nums2,monotonic))
        res = []
        for num in nums1:
            if num not in _map:
                continue
            res.append(_map[num])
        return(res)