class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # Calculate the sum of all numbers from 1 to n using the formula n * (n + 1) / 2
        expected_sum = n * (n + 1) // 2
        # Calculate the sum of squares of all numbers from 1 to n using the formula n * (n + 1) * (2n + 1) / 6
        expected_sum_of_squares = n * (n + 1) * (2 * n + 1) // 6
        
        actual_sum = sum(nums)
        actual_sum_of_squares = sum(x ** 2 for x in nums)
        
        # The difference between the expected sum and the actual sum is the missing number
        missing_number = expected_sum - actual_sum
        # The difference between the expected sum of squares and the actual sum of squares is the square of the duplicated number
        duplicated_number = (expected_sum_of_squares - actual_sum_of_squares) // missing_number
        
        return [duplicated_number, missing_number]
