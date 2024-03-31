class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        # Initialize variables
        res = 0           # Result variable to count valid subarrays
        bad_idx = left_idx = right_idx = -1  # Indices for tracking invalid and valid numbers
        
        # Iterate through the array
        for i, num in enumerate(nums):
            # If the number is not within the range [minK, maxK], update bad_idx
            if not minK <= num <= maxK:
                bad_idx = i

            # If the number is minK, update left_idx
            if num == minK:
                left_idx = i

            # If the number is maxK, update right_idx
            if num == maxK:
                right_idx = i

            # Calculate the count of valid subarrays
            res += max(0, min(left_idx, right_idx) - bad_idx)

        return res  # Return the count of valid subarrays
