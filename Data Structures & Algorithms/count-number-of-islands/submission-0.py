class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        visited = set()
        res = 0
        def dfs(i, j):
            if not len(grid) > i >= 0:
                return
            if not len(grid[0]) > j >= 0:
                return 
            if grid[i][j] == "0":
                return
            
            if (i, j) in visited:
                return

            visited.add((i, j))

            #top
            if i > 0:
                dfs(i - 1, j)
            #bottom
             

            if i < len(grid) - 1:
                dfs(i + 1, j)
            #left
            
            if j > 0:
                dfs(i, j - 1)
            
            #right
            if j < len(grid[0]) - 1:
                dfs(i, j + 1)


        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "0":
                    continue
                
                if (i,j) in visited:
                    continue
                else:
                    res += 1
                    dfs(i, j)

        
        return res