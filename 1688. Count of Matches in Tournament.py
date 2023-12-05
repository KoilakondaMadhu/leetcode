# Define a class named Solution
class Solution:
    
    # Define a method within the class to calculate the number of matches
    def numberOfMatches(self, n: int) -> int:
        # Initialize a variable to store the total number of matches
        ans = 0
        
        # Continue the loop until there is only one team left
        while n > 1:
            # Check if the number of teams is even
            if n % 2 == 0:
                # If even, add half of the teams to the total matches
                ans += n // 2
                # Update the number of teams to be half
                n = n // 2
            else:
                # If odd, add (n - 1) // 2 teams to the total matches
                ans += (n - 1) // 2
                # Update the number of teams to be ((n - 1) // 2) + 1
                n = ((n - 1) // 2) + 1
        
        # Return the total number of matches
        return ans
