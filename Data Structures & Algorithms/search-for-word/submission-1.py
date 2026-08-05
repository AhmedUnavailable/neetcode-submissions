class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        def bt(i, j, idx):
            if idx == len(word):
                return True
            
            if (i < 0 or  i >= ROWS or j < 0 or j>= COLS) or board[i][j] != word[idx]:
                return False
            
            temp = board[i][j]
            board[i][j] = "#"

            valid = (bt(i - 1, j, idx + 1)
                    or bt(i + 1, j, idx + 1)
                    or bt(i, j - 1, idx + 1)
                    or bt(i, j + 1, idx + 1))
            board[i][j] = temp
            return valid

        for i in range(ROWS):
            for j in range(COLS): 
                if board[i][j] == word[0]:
                    if bt(i, j, 0):
                        return True
        return False
                
