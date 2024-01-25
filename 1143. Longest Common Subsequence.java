class Solution {
    public int longestCommonSubsequence(String text1, String text2) {
        // Lengths of the input strings
        int length1 = text1.length();
        int length2 = text2.length();
      
        // Create a 2D array to store the lengths of longest common subsequences
        // for all subproblems, initialized with zero
        int[][] dp = new int[length1 + 1][length2 + 1];

        // Build the dp array from the bottom up
        for (int i = 1; i <= length1; ++i) {
            for (int j = 1; j <= length2; ++j) {
                // If characters match, take diagonal value and add 1
                if (text1.charAt(i - 1) == text2.charAt(j - 1)) {
                    dp[i][j] = dp[i - 1][j - 1] + 1;
                }
                // If characters do not match, take the maximum value from 
                // the left (dp[i][j-1]) or above (dp[i-1][j])
                else {
                    dp[i][j] = Math.max(dp[i - 1][j], dp[i][j - 1]);
                }
            }
        }
        // The bottom-right cell contains the length of the longest
        // common subsequence of text1 and text2
        return dp[length1][length2];
    }
}
class Solution {
public:
    // Function to find the length of the longest common subsequence in two strings.
    int longestCommonSubsequence(string text1, string text2) {
        int text1Length = text1.size(), text2Length = text2.size();
        // Create a 2D array to store lengths of common subsequence at each index.
        int dp[text1Length + 1][text2Length + 1];
      
        // Initialize the 2D array with zero.
        memset(dp, 0, sizeof dp);
      
        // Loop through both strings and fill the dp arr
