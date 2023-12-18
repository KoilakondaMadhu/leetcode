from typing import List
from math import inf

class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        # Initialize variables to keep track of the two largest and two smallest numbers
        biggest = 0
        second_biggest = 0
        smallest = inf
        second_smallest = inf
        
        # Iterate through the list of numbers
        for num in nums:
            # Check if the current number is greater than the current biggest
            if num > biggest:
                # If so, update the second biggest and the biggest
                second_biggest = biggest
                biggest = num
            else:
                # If not, update only the second biggest if the current number is greater than it
                second_biggest = max(second_biggest, num)
                
            # Check if the current number is smaller than the current smallest
            if num < smallest:
                # If so, update the second smallest and the smallest
                second_smallest = smallest
                smallest = num
            else:
                # If not, update only the second smallest if the current number is smaller than it
                second_smallest = min(second_smallest, num)
        
        # Calculate the maximum product difference and return it
        return biggest * second_biggest - smallest * second_smallest
