class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        total_slices = 0  # Variable to store the total count of arithmetic slices
        
        # Dictionary to store the dynamic programming information
        dp = [defaultdict(int) for _ in range(n)]

        # Iterate over each element in the array
        for i in range(n):
            for j in range(i):
                # Calculate the difference between the current element and the previous element
                diff = nums[i] - nums[j]

                # Update the dynamic programming dictionary
                dp[i][diff] += dp[j][diff] + 1

                # Add the count to the total slices
                total_slices += dp[j][diff]

        return total_slices
