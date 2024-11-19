from collections import defaultdict

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        count = defaultdict(int)
        cur_sum = 0
        l = 0
        
        for r in range(len(nums)):
            cur_sum += nums[r]
            count[nums[r]] += 1
            
            # If the window size exceeds k, shrink the window
            while r - l + 1 > k:
                count[nums[l]] -= 1
                if count[nums[l]] == 0:
                    del count[nums[l]]
                cur_sum -= nums[l]
                l += 1
                
            # If the window size is exactly k and all elements are unique
            if r - l + 1 == k and len(count) == k:
                res = max(res, cur_sum)
                
        return res
