class Solution:
    def numDecodings(self, s: str) -> int:
        # Handle edge case
        if not s or s[0] == "0":
            return 0
        
        # Initialize an array to store the number of ways to decode at each position
        dp = [0] * (len(s) + 1)
        dp[0] = 1  # Empty string can be decoded in one way
        
        # Fill the dp array
        for i in range(1, len(s) + 1):
            # Check if the current digit is not zero
            if s[i - 1] != "0":
                dp[i] += dp[i - 1]
            
            # Check if the current and previous digits form a valid encoding (between 10 and 26)
            if i > 1 and "10" <= s[i - 2:i] <= "26":
                dp[i] += dp[i - 2]
        
        return dp[len(s)]
