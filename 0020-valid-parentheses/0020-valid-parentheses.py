class Solution:
    def isValid(self, s: str) -> bool:
        _map = {')':'(','}':'{',']':'['}

        stack = []

        for char in s:
            if char in _map.values():
                stack.append(char)
            else:
                if not stack or stack[-1]!= _map[char]:
                    return False
                stack.pop()
        return len(stack) == 0
