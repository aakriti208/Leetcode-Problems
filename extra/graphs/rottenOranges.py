from collections import deque

class Solution(object):
    def orangesRotting(self, grid):
        row, col = len(grid), len(grid[0])
        q = deque()
        fresh = 0
        # 1. Initial Scan: Find all rotten oranges and count fresh ones
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 2:
                    q.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1

        # If no fresh oranges, it takes 0 minutes
        if fresh == 0: return 0
        
        minutes = 0
        dirs = [(0,1),(0,-1), (1,0), (-1,0)]

        # 2. Level-order BFS
        while q and fresh > 0:
            minutes += 1
            # Process ONLY the oranges that were rotten at the start of this minute
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in dirs:
                    nr, nc = r+dr, c+dc
                    if nr<0 or nr>=row or nc<0 or nc>=col or grid[nr][nc] != 1:
                        continue
                    grid[nr][nc] = 2
                    fresh -= 1
                    q.append((nr, nc))

        # Final check
        return minutes if fresh == 0 else -1




        