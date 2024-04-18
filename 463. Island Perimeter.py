class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # Initialize a set to keep track of visited cells
        visit = set()

        # Define a depth-first search (DFS) function
        def dfs(i, j):
            # Base case: if the cell is out of bounds or water, return 1
            if i >= len(grid) or j >= len(grid[0]) or i < 0 or j < 0 or grid[i][j] == 0:
                return 1
            # If the cell has already been visited, return 0
            if (i, j) in visit:
                return 0
            # Mark the cell as visited
            visit.add((i, j))
            # Initialize perimeter count for the current cell
            perim = 0
            # Recursively visit adjacent cells and update perimeter count
            perim += dfs(i, j + 1)  # Right
            perim += dfs(i + 1, j)  # Down
            perim += dfs(i, j - 1)  # Left
            perim += dfs(i - 1, j)  # Up
            return perim

        # Iterate through the grid to find the first land cell
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    # If a land cell is found, start DFS from that cell
                    return dfs(i, j)
