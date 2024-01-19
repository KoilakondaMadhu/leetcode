from typing import List

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0

        rows, cols = len(matrix), len(matrix[0])

        for i in range(1, rows):
            for j in range(cols):
                # Calculate the minimum falling path sum for each cell
                matrix[i][j] += min(matrix[i-1][max(0, j-1):min(cols, j+2)])

        # The minimum falling path sum will be the minimum value in the last row
        return min(matrix[-1])

# Example usage:
matrix1 = [[2,1,3],[6,5,4],[7,8,9]]
solution = Solution()
result1 = solution.minFallingPathSum(matrix1)
print(result1)  # Output: 13

matrix2 = [[-19,57],[-40,-5]]
result2 = solution.minFallingPathSum(matrix2)
print(result2)  # Output: -59
