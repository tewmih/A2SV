class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=0
        right=0
        longest=float("-inf")
        my_set=set()
        # if s=="":
        #     return 0

        while left<=right<len(s):

            if s[right]  not in my_set:
                my_set.add(s[right])
                right+=1
            elif s[right] in my_set: #abcda
                longest=max(longest,(right-left))
                my_set.discard(s[left])
                left+=1
        longest=max(longest,(right-left))

        return longest
            
            
        