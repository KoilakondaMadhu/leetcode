class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        
        n = len(matrix)
        m = len(matrix[0])
        heights = [0] * (m + 1)
        max_area = 0
        
        for i in range(n):
            # Update the heights array
            for j in range(m):
                if matrix[i][j] == "1":
                    heights[j] += 1
                else:
                    heights[j] = 0
            
            # Calculate the largest rectangle area for the current row
            stack = [-1]
            for j in range(m + 1):
                while heights[j] < heights[stack[-1]]:
                    h = heights[stack.pop()]
                    w = j - stack[-1] - 1
                    max_area = max(max_area, h * w)
                stack.append(j)
        
        return max_area
