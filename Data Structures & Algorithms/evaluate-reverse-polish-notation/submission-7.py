class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        for t in tokens:
            if t in "+-/*":
                a = int(s.pop())
                b = int(s.pop())

                if t == "+":
                    s.append(a + b)
                if t == "-":
                    s.append(b - a)
                if t == "/":
                    s.append(int(b  / a))
                if t == "*":
                    s.append(b * a)
            else:
                s.append(int(t))
        return s[0]