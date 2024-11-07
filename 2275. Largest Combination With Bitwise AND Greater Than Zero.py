from typing import List

class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        count = [0] * 32
        for n in candidates:
            i = 0
            while n > 0:
                if n & 1:  # Check if the ith bit is set
                    count[i] += 1
                i += 1
                n >>= 1  # Right shift to check the next bit

        return max(count)  # Return the maximum count of set bits at any position
