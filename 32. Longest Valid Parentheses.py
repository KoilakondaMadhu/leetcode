class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0

        # Initialize an array to store the length of valid parentheses ending at each position
        dp = [0] * n
        max_length = 0

        # Iterate through the string
        for i in range(1, n):
            # Check if the current character is ')'
            if s[i] == ')':
                # Case 1: "()" pattern
                if s[i - 1] == '(':
                    dp[i] = dp[i - 2] + 2 if i >= 2 else 2
                # Case 2: "(...)" pattern
                elif i - dp[i - 1] > 0 and s[i - dp[i - 1] - 1] == '(':
                    dp[i] = dp[i - 1] + 2 + (dp[i - dp[i - 1] - 2] if i - dp[i - 1] >= 2 else 0)

                # Update the maximum length
                max_length = max(max_length, dp[i])

        return max_length
