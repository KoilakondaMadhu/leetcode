from typing import List

class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        def dfs(r, c):
            if r < 0 or r >= m or c < 0 or c >= n or land[r][c] != 1:
                return
            land[r][c] = -1  # Mark as visited
            farmland[2] = max(farmland[2], r)
            farmland[3] = max(farmland[3], c)
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)
        
        m, n = len(land), len(land[0])
        result = []
        
        for i in range(m):
            for j in range(n):
                if land[i][j] == 1:
                    farmland = [i, j, i, j]  # [r1, c1, r2, c2]
                    dfs(i, j)
                    result.append(farmland)
        
        return result

# Test cases
solution = Solution()
print(solution.findFarmland([[1,0,0],[0,1,1],[0,1,1]]))  # Output: [[0,0,0,0],[1,1,2,2]]
print(solution.findFarmland([[1,1],[1,1]]))            # Output: [[0,0,1,1]]
print(solution.findFarmland([[0]]))                    # Output: []
