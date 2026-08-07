class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        
        def bt(string, op, cl):
            if op > n or cl > op:
                return 
            if len(string) == 2*n:
                res.append(string)
                return

            bt(string + "(", op + 1, cl)
            
            bt(string +")", op, cl + 1)
        
        bt("", 0, 0)

        return res
