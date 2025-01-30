class Solution:
    def isPalindrome(self, s: str) -> bool:
        reslut=""
        for i in s:
            if i.isalnum():
                i=i.lower()
                reslut+=i

        reversed=reslut [::-1]
        return reversed==reslut