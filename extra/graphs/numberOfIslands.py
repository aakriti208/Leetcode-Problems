"""We can either perform a DFS or a BFS on this problem. I'm gonna do a DFS. first, lets initialize the value of numberOfIslands to 0.
            then we go through each of the elements in the row and column. if the element at a certain position if '1', we increment the numberofislands by 1.
            and perform dfs from that node. For the DFS function, we eliminate all the nodes that dont belong to the grid. If i is a node that out of index from that grid,
            or if the current node is not 1, we return. We also change the value of the current node to '0' just so that the node is not visited again.
            Else we perform DFS on all the connections.... 
            """


class Solution(object):
    def numIslands(self, grid):
        # We first find out the size of the row and column. the row is gonna be the length of the grid and col is gonna be the length of the first grid
        if not grid: return 0
        r, c = len(grid), len(grid[0])
        dirs = [(0,1),(1,0),(0,-1),(-1,0)]
        
        def dfs(i, j):
            if i<0 or i>=r or j<0 or j>=c or grid[i][j] != '1':
                return
            grid[i][j] = '0'
            for dr, dc in dirs:
                dfs(i+dr, j+dc)

        numOfIslands = 0
        for i in range(r):
            for j in range(c):
                if grid[i][j] == '1':
                    numOfIslands += 1
                    dfs(i, j)
        return numOfIslands
        
         
    # SC: O(r*c)
    # TC: O(r*c)