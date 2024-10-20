from typing import List

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = float('inf')
        second = float('inf')
        
        for n in nums:
            if n <= first:
                first = n  # update the smallest number
            elif n <= second:
                second = n  # update the second smallest number
            else:
                return True  # found a number greater than both first and second
        
        return False  # no such triplet found
