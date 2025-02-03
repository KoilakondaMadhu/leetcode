from typing import List

class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0  # Handle empty list case
        
        ans, inc, dec = 1, 1, 1  # Initialize ans to 1 to handle single element arrays correctly
        
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                inc += 1
                dec = 1
            elif nums[i] < nums[i - 1]:
                inc = 1
                dec += 1
            else:
                inc = dec = 1
            
            ans = max(ans, inc, dec)
        
        return ans
