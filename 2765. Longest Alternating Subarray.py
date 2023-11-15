# 2765. Longest Alternating Subarray
# Easy
# Topics
# Companies
# Hint
# You are given a 0-indexed integer array nums. A subarray s of length m is called alternating if:

# m is greater than 1.
# s1 = s0 + 1.
# The 0-indexed subarray s looks like [s0, s1, s0, s1,...,s(m-1) % 2]. In other words, s1 - s0 = 1, s2 - s1 = -1, s3 - s2 = 1, s4 - s3 = -1, and so on up to s[m - 1] - s[m - 2] = (-1)m.
# Return the maximum length of all alternating subarrays present in nums or -1 if no such subarray exists.

# A subarray is a contiguous non-empty sequence of elements within an array.

 class Solution(object):
    def alternatingSubarray(self, nums):
        res = -1  # Initialize the result variable to -1

        # Outer loop iterates over each index i in the range of the length of nums
        for i in range(len(nums)):            
            # Inner loop iterates over each index j starting from i+1 to the length of nums
            for j in range(i + 1, len(nums)):
                # Check if the alternating condition is satisfied
                if nums[j - 1] != nums[j] + (-1) ** (j - i):
                    break  # If the condition is not satisfied, break out of the inner loop
                res = max(res, j - i + 1)  # Update the result with the length of the alternating subarray

        return res  # Return the final result


# Example 1:

# Input: nums = [2,3,4,3,4]
# Output: 4
# Explanation: The alternating subarrays are [3,4], [3,4,3], and [3,4,3,4]. The longest of these is [3,4,3,4], which is of length 4.
# Example 2:

# Input: nums = [4,5,6]
# Output: 2
# Explanation: [4,5] and [5,6] are the only two alternating subarrays. They are both of length 2.
 

# Constraints:

# 2 <= nums.length <= 100
# 1 <= nums[i] <= 104
