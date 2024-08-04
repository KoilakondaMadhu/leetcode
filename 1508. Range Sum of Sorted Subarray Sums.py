import heapq

class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        min_heap = []
        
        # Generate all subarray sums
        for i in range(n):
            s = 0
            for j in range(i, n):
                s += nums[j]
                heapq.heappush(min_heap, s)
        
        # Extract the range [left-1, right] smallest sums from the heap
        mod = 10**9 + 7
        result = 0
        for _ in range(right):
            if left > 1:
                heapq.heappop(min_heap)
                left -= 1
            else:
                result = (result + heapq.heappop(min_heap)) % mod
        
        return result
