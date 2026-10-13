class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def bt(s, c, o):
            if n < o or o < c:
                return

            if len(s) == 2*n:
                res.append(s)
                return
            
            bt(s + "(", c, o + 1)
            bt(s + ")", c + 1, o)

            return    

        bt("", 0, 0)

        return res