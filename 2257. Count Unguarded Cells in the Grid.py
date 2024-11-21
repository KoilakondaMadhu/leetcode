from typing import List

class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        # Initialize the matrix
        mat = [[0 for _ in range(n)] for _ in range(m)]
        
        # Mark guards and walls
        for i, j in guards:
            mat[i][j] = 1  # Guard
        for i, j in walls:
            mat[i][j] = -1  # Wall
        
        # Helper to mark guard lines
        def mark_guarded(i, j, di, dj):
            while 0 <= i < m and 0 <= j < n:
                if mat[i][j] == 1 or mat[i][j] == -1:  # Stop at guard or wall
                    break
                if mat[i][j] == 0:  # Mark as guarded
                    mat[i][j] = 2
                i += di
                j += dj

        # Directions: right, down, left, up
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for i, j in guards:
            for di, dj in directions:
                mark_guarded(i + di, j + dj, di, dj)

        # Count unguarded cells
        return sum(cell == 0 for row in mat for cell in row)
