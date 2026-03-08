class Solution(object):
    def numIslands(self, grid):
        r, c = len(grid), len(grid[0])

        def dfs(i, j):
            if i<0 or i>=r or j<0 or j>=c or grid[i][j] != '1':
                return
            else:
                grid[i][j] = '0'
                dfs(i, j+1)
                dfs(i+1, j)
                dfs(i-1, j)
                dfs(i, j-1)

        numOfIslands = 0
        for i in range(r):
            for j in range(c):
                if grid[i][j] == '1':
                    numOfIslands += 1
                    dfs(i, j)
        return numOfIslands
        
         
        