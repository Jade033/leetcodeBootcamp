# leetcode 200 Number of Islands
# Author Tianyi Xu
from collections import deque
class Solution:
    # dfs approach
    def numIslands(self, grid) -> int:
        numOfIsles = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    numOfIsles += 1
        return numOfIsles

    def dfs(self, grid, r, c):
        if (
            (r < 0)
             or (c < 0) 
             or (r >= len(grid)) 
             or (c >= len(grid[0])) 
             or (grid[r][c] != '1')
             ) :
            return 
        else:
            grid[r][c] = '0'
            self.dfs(grid, r - 1, c)
            self.dfs(grid, r + 1, c)
            self.dfs(grid, r, c - 1)
            self.dfs(grid, r, c + 1)

    # bfs approach
    def numIslandsBfs(self, grid):
        numOfIsles = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == '1':
                    neighbors = deque()
                    neighbors.append((r,c))
                    grid[r][c] = '0'
                    while (neighbors):
                        tempRow, tempCol = neighbors.popleft()
                        if ((tempRow-1) >= 0) and (grid[tempRow-1][tempCol] == '1'):
                            neighbors.append((tempRow - 1, tempCol))
                            grid[tempRow-1][tempCol] = '0'
                        if ((tempRow+1) < len(grid)) and (grid[tempRow+1][tempCol] == '1'):
                            neighbors.append((tempRow + 1, tempCol))
                            grid[tempRow+1][tempCol] = '0'
                        if ((tempCol-1) >= 0) and (grid[tempRow][tempCol-1] == '1'):
                            neighbors.append((tempRow, tempCol - 1))
                            grid[tempRow][tempCol-1] = '0'
                        if ((tempCol+1) < len(grid[0])) and (grid[tempRow][tempCol+1] == '1'):
                            neighbors.append((tempRow, tempCol + 1))
                            grid[tempRow][tempCol+1] = '0'
                    numOfIsles += 1
        return numOfIsles
 