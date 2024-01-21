class Solution:
    def rob(self, nums):
        if not nums:
            return 0
        
        n = len(nums)
        
        # Create an array to store the maximum amount of money that can be robbed at each house
        dp = [0] * n
        
        # Base cases
        dp[0] = nums[0]
        if n > 1:
            dp[1] = max(nums[0], nums[1])
        
        # Dynamic programming to fill in the rest of the array
        for i in range(2, n):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        
        # The maximum amount of money that can be robbed is the last element in the array
        return dp[-1]

# Example usage:
solution = Solution()
nums1 = [1, 2, 3, 1]
nums2 = [2, 7, 9, 3, 1]
print(solution.rob(nums1))  # Output: 4
print(solution.rob(nums2))  # Output: 12
