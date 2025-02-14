class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_palendrom(left,right):
            if left<right:
                if s[left]!=s[right]:
                    return False
                else:
                    return True
            else:
                return True

        left =0
        right=len(s)-1
        count=0
        while left<right:
            if s[left]!=s[right]:
                if is_palendrom(left + 1, right):
                    left+=1
                    count+=1
                elif is_palendrom(left, right - 1):
                    right-=1
                    count+=1
                else:
                    return False
            else:            
                left+=1
                right-=1
            if count>1:
                return False
        
        return True

            
