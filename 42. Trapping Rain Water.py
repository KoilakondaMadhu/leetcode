class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        n = len(height)
        left_max = [0] * n
        right_max = [0] * n
        water_trapped = 0
        
        # Find the maximum height on the left of each bar
        left_max[0] = height[0]
        for i in range(1, n):
            left_max[i] = max(left_max[i - 1], height[i])
        
        # Find the maximum height on the right of each bar
        right_max[n - 1] = height[n - 1]
        for i in range(n - 2, -1, -1):
            right_max[i] = max(right_max[i + 1], height[i])
        
        # Calculate the amount of water trapped above each bar
        for i in range(n):
            water_trapped += min(left_max[i], right_max[i]) - height[i]
        
        return water_trapped
