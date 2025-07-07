from typing import List
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        cnt = {}
        for i in nums:
            cnt[i] = cnt.get(i, 0) + 1
        freq_list = []
        for key, val in cnt.items():
            freq_list.append((val, key))  # (frequency, element)

        freq_list.sort(reverse=True)  # sort by frequency descending

        result = []
        for i in range(k):
            result.append(freq_list[i][1])  # take element, not frequency
        return result

        
        
