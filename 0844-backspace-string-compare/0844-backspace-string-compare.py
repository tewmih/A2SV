class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack1  = []
        stack2 = []

        for char in s:
            if char != '#':
                stack1.append(char)
            else:
                if not stack1:
                    continue
                else:
                    stack1.pop()
                
        
        for char in t:
            if char != '#':
                stack2.append(char)
            else:
                if not stack2:
                    continue
                else:
                    stack2.pop()
        return stack1 == stack2