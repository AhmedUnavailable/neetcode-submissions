class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        R, C = len(board), len(board[0])
        res = False

        def bt(r, c, i):
            
            if r < 0  or c < 0 or r >= R  or c >= C:
                return
            
            if board[r][c] != word[i] or board[r][c] == "#":
                return
            if i == len(word) - 1:
                nonlocal res
                res = True
                return 

            board[r][c] = '#'        

            bt(r + 1, c, i + 1)
            bt(r - 1, c, i + 1)
            bt(r, c + 1, i + 1)
            bt(r, c - 1, i + 1)

            board[r][c] = word[i]

        for r in range(R):
            for c in range(C):
                if board[r][c] == word[0]: 
                    bt(r,c, 0)
        
        return res