from collections import Counter

class Solution:
    def maxDifference(self, s: str) -> int:
        freq = Counter(s)
        odd_max = float('-inf')
        even_min = float('inf')

        for count in freq.values():
            if count % 2 == 1:
                odd_max = max(odd_max, count)
            else:
                even_min = min(even_min, count)

        return odd_max - even_min
