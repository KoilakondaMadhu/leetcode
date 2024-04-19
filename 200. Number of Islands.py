from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        def dfs(row, col):
            # Base case: if out of bounds or current cell is water ('0')
            if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col] == '0':
                return
            # Mark current cell as visited
            grid[row][col] = '0'
            # Explore adjacent cells
            dfs(row+1, col)  # down
            dfs(row-1, col)  # up
            dfs(row, col+1)  # right
            dfs(row, col-1)  # left
        
        island_count = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == '1':
                    island_count += 1
                    dfs(row, col)
        
        return island_count
