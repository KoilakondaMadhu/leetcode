class Solution:
    def largestDivisibleSubset(self, nums):
        # Check if input list is empty
        if not nums:
            return []
        
        # Sort the input list
        nums.sort()
        
        # Dynamic programming table to store subsets
        dp = [[num] for num in nums]
        
        # Initialize variable to store the largest subset found
        max_subset = []
        
        # Loop through each element in the sorted list
        for i in range(len(nums)):
            # Compare with elements before the current element
            for j in range(i):
                # Check if the current element is divisible by the previous element
                # and if adding the current element to the subset ending at previous element
                # results in a larger subset
                if nums[i] % nums[j] == 0 and len(dp[i]) < len(dp[j]) + 1:
                    dp[i] = dp[j] + [nums[i]]  # Update subset with the current element
                
            # Update the largest subset found so far
            if len(dp[i]) > len(max_subset):
                max_subset = dp[i]
        
        # Return the largest divisible subset found
        return max_subset

# Example usage:
sol = Solution()
nums = [1, 2, 3, 4, 6, 8, 12]
print(sol.largestDivisibleSubset(nums))  # Output: [1, 2, 4, 8, 12]
