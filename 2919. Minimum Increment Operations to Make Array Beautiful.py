class Solution:
    def minIncrementOperations(self, nums: List[int], k: int) -> int:
        
        @cache
        def dfs(i) -> int:
            if i >= len(nums)-2 : return 0
                        
            A = max(0, k - nums[i])   + dfs(i+1)
            B = max(0, k - nums[i+1]) + dfs(i+2) if i+1 < len(nums) else inf
            C = max(0, k - nums[i+2]) + dfs(i+3) if i+2 < len(nums) else inf
            
            return min(A, B, C)
        
        return dfs(0)
