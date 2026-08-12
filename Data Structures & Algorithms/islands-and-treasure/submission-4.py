class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        R, C = len(grid), len(grid[0])
        visited = set()
        q = deque()


        def addCell(r, c):
            if (min(r, c) < 0 or r == R or c == C or
                (r, c) in visited or grid[r][c] == -1
            ):
                return
            visited.add((r, c))
            q.append((r, c))


        for i in range(R):
            for j in range(C):
                if grid[i][j] == 0:
                    q.append((i, j))
                    visited.add((i,j))
                    
        
        depth = 0

        while q:
            clen = len(q)

            for _ in range(clen):
                r, c = q.popleft()

            
                
                grid[r][c] = depth  
                
                addCell(r + 1, c)
                addCell(r - 1, c)
                addCell(r , c - 1)
                addCell(r , c + 1)

            depth += 1