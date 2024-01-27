class Solution {
public:
    int kInversePairs(int n, int k) {
        // Initialize a 2D dynamic programming array with dimensions (n+1)x(k+1)
        int dp[1001][1001] = {1};  // Initialize the first element to 1
        
        // Iterate over the number of elements (i) from 1 to n
        for (int i = 1; i <= n; i++) {
            // Iterate over the number of inverse pairs (j) from 0 to k
            for (int j = 0; j <= k; j++) {
                // Iterate over the number of inverse pairs formed by the last element (x)
                for (int x = 0; x <= min(j, i - 1); x++) {
                    // Update dp[i][j] based on the previous values
                    if (j - x >= 0) {
                        dp[i][j] = (dp[i][j] + dp[i - 1][j - x]) % 1000000007;
                    }
                }
            }
        }

        // Return the final result representing the number of arrays with exactly k inverse pairs
        return dp[n][k];
    }
};
