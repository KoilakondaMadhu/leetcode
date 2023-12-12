from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Sort the input list in ascending order
        nums.sort()

        # Get the two largest elements in the sorted list
        x = nums[-1]  # Largest element
        y = nums[-2]  # Second largest element

        # Calculate the maximum product by subtracting 1 from each of the largest elements and multiplying them
        result = (x - 1) * (y - 1)

        return result
