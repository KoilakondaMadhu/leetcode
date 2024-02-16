from typing import List
from collections import Counter

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        # Count the frequency of each element in the array
        freq = Counter(arr)
        
        # Create a list to store the frequency counts of frequencies (meta-frequency counts)
        # The index represents the frequency and the value at that index represents
        # how many elements have that frequency
        freq_list = [0] * (len(arr) + 1)
        
        # Populate the freq_list
        for m, f in freq.items():
            freq_list[f] += 1
        
        # Initialize the result with the total number of unique elements
        res = len(freq)
        
        # Traverse the freq_list starting from frequency 1
        for f in range(1, len(freq_list)):
            remove = freq_list[f]  # Number of elements with frequency f
            
            # If we can remove all elements with frequency f using k removals
            if k >= f * remove:
                k -= f * remove  # Update remaining removals
                res -= remove    # Update result by removing all elements with frequency f
            else:
                # If we cannot remove all elements with frequency f using k removals,
                # calculate how many elements we can remove
                remove = k // f
                res -= remove  # Update result by removing 'remove' elements
                break  # No need to continue, as we cannot remove any more elements
        
        return res

# Example usage:
# arr = [4, 3, 1, 1, 3, 3, 2], k = 3
# Output: 2
# Explanation: Remove 1 and 2. 2 is the least number of unique integers left.
