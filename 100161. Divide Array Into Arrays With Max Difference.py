from typing import List

class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        # Sort the array
        nums.sort()
        
        n = len(nums)
        result = []
        
        # Iterate through the sorted array in steps of 3
        for i in range(0, n, 3):
            # Check if the current subarray has a difference less than or equal to k
            if i + 2 < n and nums[i + 2] - nums[i] <= k:
                # If the conditions are satisfied, append the subarray to the result
                result.append(nums[i:i + 3])
            else:
                # If it's not possible to satisfy the conditions, return an empty array
                return []
        
        return result

# Example usage:
# nums = [1, 3, 4, 8, 7, 9, 3, 5, 1]
# k = 2
# sol = Solution()
# result = sol.divideArray(nums, k)
# print(result)












# Explore
# Problems
# Contest
# Discuss
# Interview
# Store
# 27

# avatar
# 100161. Divide Array Into Arrays With Max Difference
# User Accepted:3492
# User Tried:4094
# Total Accepted:3522
# Total Submissions:5496
# Difficulty:Medium
# You are given an integer array nums of size n and a positive integer k.

# Divide the array into one or more arrays of size 3 satisfying the following conditions:

# Each element of nums should be in exactly one array.
# The difference between any two elements in one array is less than or equal to k.
# Return a 2D array containing all the arrays. If it is impossible to satisfy the conditions, return an empty array. And if there are multiple answers, return any of them.

 

# Example 1:

# Input: nums = [1,3,4,8,7,9,3,5,1], k = 2
# Output: [[1,1,3],[3,4,5],[7,8,9]]
# Explanation: We can divide the array into the following arrays: [1,1,3], [3,4,5] and [7,8,9].
# The difference between any two elements in each array is less than or equal to 2.
# Note that the order of elements is not important.
# Example 2:

# Input: nums = [1,3,3,2,7,3], k = 3
# Output: []
# Explanation: It is not possible to divide the array satisfying all the conditions.
 

# Constraints:

# n == nums.length
# 1 <= n <= 105
# n is a multiple of 3.
# 1 <= nums[i] <= 105
# 1 <= k <= 105
# Python3	
# from typing import List

# class Solution:
#     def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
#         # Sort the array
#         nums.sort()
        
#         n = len(nums)
#         result = []
        
#         for i in range(0, n, 3):
#             # Check if current subarray has a difference less than or equal to k
#             if i + 2 < n and nums[i + 2] - nums[i] <= k:
#                 result.append(nums[i:i + 3])
#             else:
#                 # If not possible to satisfy conditions, return an empty array
#                 return []
        
#         return result

# # Example usage:
# # nums = [1, 3, 4, 8, 7, 9, 3, 5, 1]
# # k = 2
# # sol = Solution()
# # result = sol.divideArray(nums, k)
# # print(result)

# 1
# from typing import List
# 2
# ​
# 3
# class Solution:
# 4
#     def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
# 5
#         # Sort the array
# 6
#         nums.sort()
# 7
        
# 8
#         n = len(nums)
# 9
#         result = []
# 10
        
# 11
#         for i in range(0, n, 3):
# 12
#             # Check if current subarray has a difference less than or equal to k
# 13
#             if i + 2 < n and nums[i + 2] - nums[i] <= k:
# 14
#                 result.append(nums[i:i + 3])
# 15
#             else:
# 16
#                 # If not possible to satisfy conditions, return an empty array
# 17
#                 return []
# 18
        
# 19
#         return result
# 20
# ​
# 21
# # Example usage:
# 22
# # nums = [1, 3, 4, 8, 7, 9, 3, 5, 1]
# 23
# # k = 2
# 24
# # sol = Solution()
# 25
# # result = sol.divideArray(nums, k)
# 26
# # print(result)
# 27
# ​
#   Custom Testcase
# Copyright © 2023 LeetCode
# Help Center
# Jobs
# Bug Bounty
# Online Interview
# Students
# Terms
# Privacy Policy
# United StatesUnited States
