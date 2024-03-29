from typing import List

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        max_element = max(nums)
        ans = start = max_elements_in_window = 0

        for end in range(len(nums)):
            if nums[end] == max_element:
                max_elements_in_window += 1
            while max_elements_in_window > k:
                # If the number of maximum elements in the window exceeds k,
                # move the start pointer forward until it satisfies the condition again.
                if nums[start] == max_element:
                    max_elements_in_window -= 1
                start += 1
            # For each valid subarray ending at 'end', add the number of valid subarrays to the answer.
            ans += (end - start + 1)
        return ans
