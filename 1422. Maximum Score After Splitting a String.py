class Solution:
    def maxScore(self, s: str) -> int:
        # Initialize the variable to store the maximum score
        ans = 0
        
        # Iterate through the characters of the string up to the second-to-last character
        for i in range(len(s) - 1):
            # Initialize the variable to calculate the current score
            curr = 0
            
            # Count the number of "0"s before the current index (i)
            for j in range(i + 1):
                if s[j] == "0":
                    curr += 1
            
            # Count the number of "1"s after the current index (i)
            for j in range(i + 1, len(s)):
                if s[j] == "1":
                    curr += 1
            
            # Update the maximum score with the maximum value between its current value and the calculated score
            ans = max(ans, curr)
    
        # Return the final maximum score
        return ans
