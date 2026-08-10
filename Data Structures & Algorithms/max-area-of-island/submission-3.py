class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        R, C = len(grid), len(grid[0])

        visited = set()

        def dfs(r, c):
            if r < 0 or c < 0 or c >= C or r >= R or (r, c) in visited or grid[r][c] == 0:
                return 0
            
            visited.add((r, c))

            return(
                1 + dfs(r - 1, c)
                + dfs(r + 1, c)
                + dfs(r, c - 1)
                + dfs(r, c + 1)
            )
            

        for r in range(R):
            for c in range(C):
                res = max(dfs(r, c), res)
        
        return res
        

