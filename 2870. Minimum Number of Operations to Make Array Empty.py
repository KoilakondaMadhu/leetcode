from collections import Counter
from math import ceil
from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        # Count occurrences of each element in the input list
        counter = Counter(nums)
        
        # Initialize the answer variable to keep track of the minimum operations
        ans = 0
        
        # Iterate through the counts of each unique element in the input list
        for c in counter.values():
            # If any element occurs exactly once, it's not possible to achieve the goal
            if c == 1: 
                return -1
            
            # Calculate the number of operations required for the current count and add it to the answer
            ans += ceil(c / 3)
        
        # Return the total number of operations needed to satisfy the conditions
        return ans
