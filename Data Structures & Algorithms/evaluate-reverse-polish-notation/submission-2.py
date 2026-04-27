class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        sym = {"+", "*", "-", "/"}

        for i in tokens:
            if i in sym:
                a = int(stack.pop())
                b = int(stack.pop())
                
                if i == "+":
                    stack.append(a + b)
                elif i == "-":
                    stack.append(b - a)
                elif i == "/":
                    stack.append(b / a)
                elif i == "*":
                    stack.append(a * b)
                continue
            
            stack.append(i)
        
        return int(stack[-1])
        