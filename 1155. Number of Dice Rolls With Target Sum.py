import java.util.Arrays;

class Solution {
    public int numRollsToTarget(int n, int k, int target) {
        // Create a 2D array to store intermediate results
        int[][] dp = new int[n + 1][target + 1];
        
        // Initialize the array with -1, indicating that the result is not computed yet
        for (int[] i : dp) {
            Arrays.fill(i, -1);
        }
        
        // Call the recursive helper function and return the result
        return dfs(n, k, target, dp);
    }

    private int dfs(int n, int k, int target, int[][] dp) {
        // Base case: If the remaining dice count or target sum is negative, no valid ways
        if (n < 0 || target < 0)
            return 0;
        
        // Base case: If no more dice to roll and target sum is reached, one valid way
        if (n == 0 && target == 0)
            return 1;

        // Check if the result for the current state is already computed
        if (dp[n][target] != -1)
            return dp[n][target];

        // Initialize the count of ways to reach the target sum
        int ways = 0;
        
        // Iterate over each face of the die and recursively calculate ways
        for (int i = 1; i <= k; i++) {
            ways = (ways + dfs(n - 1, k, target - i, dp)) % 1_000_000_007;
        }

        // Save the result in the dp array to avoid redundant calculations
        dp[n][target] = ways;
        
        // Return the total ways to reach the target sum
        return ways;
    }
}
