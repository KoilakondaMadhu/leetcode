from collections import defaultdict
from typing import List

class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        # Create a defaultdict with lists as default values to store groups of diagonal elements
        groups = defaultdict(list)
        
        # Iterate through the matrix in reverse order to start from the bottom-left corner
        for row in range(len(nums) - 1, -1, -1):
            for col in range(len(nums[row])):
                # Calculate the diagonal index based on the current row and column
                diagonal = row + col
                # Append the element to the corresponding diagonal group
                groups[diagonal].append(nums[row][col])
                
        # Initialize an empty list to store the final result
        ans = []
        # Initialize a variable to traverse through the diagonal groups
        curr = 0
        
        # Continue adding elements to the result list as long as there are diagonal groups
        while curr in groups:
            # Extend the result list with the elements from the current diagonal group
            ans.extend(groups[curr])
            # Move to the next diagonal group
            curr += 1

        # Return the final result list
        return ans




# Given a 2D integer array nums, return all elements of nums in diagonal order as shown in the below images.

 

# Example 1:


# Input: nums = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,4,2,7,5,3,8,6,9]
# Example 2:


# Input: nums = [[1,2,3,4,5],[6,7],[8],[9,10,11],[12,13,14,15,16]]
# Output: [1,6,2,8,7,3,9,4,12,10,5,13,11,14,15,16]
 

# Constraints:

# 1 <= nums.length <= 105
# 1 <= nums[i].length <= 105
# 1 <= sum(nums[i].length) <= 105
