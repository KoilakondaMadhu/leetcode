from typing import List

class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        # Get the length of the array
        n = len(nums)
        
        # Sort the array in ascending order
        nums.sort()
        
        # Initialize pointers and variables
        left = 0      # Left pointer for the sliding window
        right = 0     # Right pointer for the sliding window
        dist = 0      # Distinct elements in the current window
        ans = 0       # Maximum frequency found so far
        
        # Iterate through the array using the sliding window approach
        while right < n:
            # Calculate the difference in values between consecutive elements
            if right > 0 and nums[right] != nums[right - 1]:
                dist += (right - left) * (nums[right] - nums[right - 1])
            
            # Move the right pointer to the next element
            right += 1
            
            # Shrink the window if the distinct elements exceed the allowed operations (k)
            while dist > k:
                dist -= nums[right - 1] - nums[left]
                left += 1
            
            # Update the maximum frequency
            if right - left > ans:
                ans = right - left
        
        # Return the maximum frequency found
        return ans



# he frequency of an element is the number of times it occurs in an array.

# You are given an integer array nums and an integer k. In one operation, you can choose an index of nums and increment the element at that index by 1.

# Return the maximum possible frequency of an element after performing at most k operations.

 

# Example 1:

# Input: nums = [1,2,4], k = 5
# Output: 3
# Explanation: Increment the first element three times and the second element two times to make nums = [4,4,4].
# 4 has a frequency of 3.
# Example 2:

# Input: nums = [1,4,8,13], k = 5
# Output: 2
# Explanation: There are multiple optimal solutions:
# - Increment the first element three times to make nums = [4,4,8,13]. 4 has a frequency of 2.
# - Increment the second element four times to make nums = [1,8,8,13]. 8 has a frequency of 2.
# - Increment the third element five times to make nums = [1,4,13,13]. 13 has a frequency of 2.
# Example 3:

# Input: nums = [3,9,6], k = 2


# Output: 1


# Case 1

# Input
# nums =
# [1,2,4]
# k =
# 5
# Output
# 3
# Expected
# 3
