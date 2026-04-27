class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        col_set = defaultdict(set)
        row_set = defaultdict(set)
        sqr_set = defaultdict(set)

        

        for i in range(9):
            for j in range(9):
                curr = board[i][j]
                
                if curr == ".":
                    continue
                if curr in col_set[j]:
                    return False
                if curr in row_set[i]:
                    return False
                
                
                if curr in sqr_set[i//3, j//3]:
                    return False

                row_set[i].add(curr)
                col_set[j].add(curr)
                sqr_set[i//3, j//3].add(curr)
        return True

