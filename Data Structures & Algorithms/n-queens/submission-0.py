class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []

        colset = set()
        posset = set()
        negset = set()  

        board = [["."] * n for _ in range(n)]

        def bt(r):
            
            
            if r == n:
                temp = ["".join(row) for row in board]
                
                res.append(temp)
                return
            
            for c in range(n):
                if c in colset or (r + c) in posset or (r - c) in negset:
                    continue
                
                colset.add(c)
                posset.add(r + c)
                negset.add(r - c)
                board[r][c] = "Q"

                bt(r + 1)
                
                colset.remove(c)
                posset.remove(r + c)
                negset.remove(r - c)
                board[r][c] = "."
        bt(0)

        return res
