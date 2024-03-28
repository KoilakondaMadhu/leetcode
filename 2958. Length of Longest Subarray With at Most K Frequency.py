from typing import List
from collections import Counter

class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        frequency = Counter()
        start = 0
        max_length = 0  # Variable to store the maximum length of subarray with elements occurring at least k times
        chars_with_freq_over_k = 0
        for end in range(n):
            frequency[nums[end]] += 1
            if frequency[nums[end]] == k + 1:
                chars_with_freq_over_k += 1
            while chars_with_freq_over_k:
                frequency[nums[start]] -= 1
                if frequency[nums[start]] == k:
                    chars_with_freq_over_k -= 1
                start += 1
            max_length = max(max_length, end - start + 1)  # Update max_length
        return max_length
