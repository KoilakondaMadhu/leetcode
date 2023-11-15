# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Sort the array in ascending order
        nums.sort()
        
        # Get the middle element (majority element)
        m = len(nums) // 2
        
        # Return the majority element
        return nums[m]

      
# Example 1:

# Input: nums = [3,2,3]
# Output: 3
# Example 2:

# Input: nums = [2,2,1,1,1,2,2]
# Output: 2
 

# Constraints:

# n == nums.length
# 1 <= n <= 5 * 104
# -109 <= nums[i] <= 109
