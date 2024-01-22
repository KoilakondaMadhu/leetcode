class Solution:
    def findErrorNums(self, nums):
        # Initialize variables to store the duplicated and missing numbers
        dup, missing = -1, -1
        
        # Iterate through numbers from 1 to n
        for i in range(1, len(nums) + 1):
            # Count occurrences of the current number in the array
            count = nums.count(i)
            
            # If the count is 2, it means the current number is duplicated
            if count == 2:
                dup = i
            # If the count is 0, it means the current number is missing
            elif count == 0:
                missing = i
        
        # Return the result as an array containing the duplicated and missing numbers
        return [dup, missing]
