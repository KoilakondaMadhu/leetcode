from collections import defaultdict
from typing import List

class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        # Create a dictionary to store the counts of each number
        counts = defaultdict(int)
        
        # Calculate the target count, which is 1/4th of the length of the array
        target = len(arr) // 4
        
        # Iterate through the array
        for num in arr:
            # Increment the count of the current number
            counts[num] += 1
            
            # Check if the count of the current number exceeds the target
            if counts[num] > target:
                # If it does, return the current number as it is the special integer
                return num
        
        # If no special integer is found, return -1
        return -1
