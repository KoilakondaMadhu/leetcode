public class Solution {
    public int findRotateSteps(String ring, String key) {
        int n = ring.length(); // Length of the ring
        int m = key.length(); // Length of the key
        int[][] dp = new int[m + 1][n]; // Dynamic programming table
        
        // Dynamic programming loop
        for (int i = m - 1; i >= 0; i--) { // Loop through the key characters in reverse order
            for (int j = 0; j < n; j++) { // Loop through each position on the ring
                dp[i][j] = Integer.MAX_VALUE; // Initialize the minimum steps to maximum possible value
                for (int k = 0; k < n; k++) { // Loop through each position on the ring to find possible matches
                    if (ring.charAt(k) == key.charAt(i)) { // Check if the character on the ring matches the current key character
                        int diff = Math.abs(j - k); // Calculate the absolute difference between current and target positions
                        int step = Math.min(diff, n - diff); // Calculate the minimum steps needed considering the ring as circular
                        dp[i][j] = Math.min(dp[i][j], step + dp[i + 1][k]); // Update the minimum steps needed for the current key character
                    }
                }
            }
        }
        
        // Return the minimum steps needed to spell out the entire key starting from the first character on the ring
        return dp[0][0] + m; // Add the length of the key as each key character requires one step
    }
}
