class Solution:
    #17:43
    def isValid(self, s: str) -> bool:
        closeToOpen = {"]":"[", "}":"{", ")":"("}

        stack = []

        for i in range(len(s)):
            if s[i] in closeToOpen:
                if not stack:
                    return False
                if stack[-1] == closeToOpen[s[i]]:
                    stack.pop()
                else: 
                    return False
            else:
                stack.append(s[i])
        

        if stack:
            return False
        else:
            return True