from typing import List  # Make sure to import List from the 'typing' module

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        # Find the maximum number of candies among all children
        maxCandies = max(candies)
        
        # Initialize an empty list to store the boolean results
        result = []
        
        # Iterate through each child's candies
        for i in range(len(candies)):
            # Check if the current child, with extra candies, can have the maximum candies
            result.append(candies[i] + extraCandies >= maxCandies)
        
        # Return the list of boolean values indicating whether each child can have the maximum candies
        return result
