class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Initialize a list to count occurrences of each number
        cnt = [0] * (len(nums) + 1)
        
        # Iterate through the numbers in the list
        for num in nums:
            # Increment the count of the current number
            cnt[num] += 1
            
            # If the count of the current number is greater than 1,
            # it means it's a duplicate, so return it
            if cnt[num] > 1:
                return num
        
        # If no duplicates are found, return the length of the list (just a placeholder)
        return len(nums)  # comments
