class Solution:
    def climbStairs(self, n: int) -> int:
        # Initialize variables to keep track of the number of ways to reach the current step
        one, two = 1, 1

        # Iterate from 0 to n-2 (n-1 times) since we've already initialized for the first two steps
        for i in range(n - 1):
            # Store the current value of 'one' in a temporary variable
            temp = one

            # Update 'one' to be the sum of the current 'one' and 'two'
            one = one + two

            # Update 'two' to be the previous value of 'one' (stored in the temporary variable)
            two = temp

        # 'one' now contains the number of ways to reach the nth step
        return one
