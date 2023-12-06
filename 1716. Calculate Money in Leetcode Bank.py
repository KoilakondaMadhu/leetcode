# Define a class named Solution
class Solution:
    
    # Define a method within the class to calculate total money
    def totalMoney(self, n: int) -> int:
        # Initialize a variable to store the total money
        ans = 0
        
        # Initialize a variable to represent the amount saved on Mondays
        monday = 1
        
        # Continue the loop until the total number of weeks becomes zero
        while n > 0:
            # Iterate over the days of the week, up to a maximum of 7 or the remaining number of weeks
            for day in range(min(n, 7)):
                # Add the amount saved on the current day to the total money
                ans += monday + day
            
            # Decrease the remaining number of weeks by 7
            n -= 7
            
            # Increment the amount saved on Mondays by 1 for the next week
            monday += 1

        # Return the total amount of money
        return ans
