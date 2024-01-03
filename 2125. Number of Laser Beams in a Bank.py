from typing import List

class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        # Initialize prev with the count of "1"s in the first string
        prev = bank[0].count("1")
        
        # Initialize the result variable
        res = 0
        
        # Iterate over the strings in the bank starting from the second string
        for i in range(1, len(bank)):
            # Count the number of "1"s in the current string
            curr = bank[i].count("1")
            
            # Check if there is at least one "1" in the current string
            if curr:
                # Update the result by adding the product of prev and curr
                res += (prev * curr)
                
                # Update prev with the count of "1"s in the current string
                prev = curr
        
        # Return the final result
        return res
