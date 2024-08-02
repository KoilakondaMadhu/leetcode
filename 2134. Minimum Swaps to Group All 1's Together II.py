from typing import List

class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        # Step 1: Count the total number of 1's in the array
        k = nums.count(1)
        
        # If there are no 1's or the entire array is 1's, no swaps are needed
        if k == 0 or k == len(nums):
            return 0

        n = len(nums)
        
        # Step 2: Calculate the number of 1's in the initial window of size k
        current_ones = sum(nums[:k])
        max_ones_in_window = current_ones
        
        # Step 3: Use a sliding window to find the maximum number of 1's in any window of size k
        for i in range(1, n):
            # Update the count of 1's in the current window
            # Add the next element in the window (i + k - 1) % n ensures circular array
            current_ones += nums[(i + k - 1) % n]
            # Remove the element that is no longer in the window
            current_ones -= nums[i - 1]
            # Update the maximum number of 1's found in any window of size k
            max_ones_in_window = max(max_ones_in_window, current_ones)
        
        # Step 4: Calculate the minimum number of swaps required
        # This is the total number of 1's minus the maximum number of 1's in any window of size k
        return k - max_ones_in_window
