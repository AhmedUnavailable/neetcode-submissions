class Solution:
    def isValid(self, s: str) -> bool:

        cto = {
            "}": "{",
            ")": "(",
            "]": "["
        }
        
        stack = []
        for i in s:
            if i in cto:
                if stack and stack[-1] == cto[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return False if stack else True