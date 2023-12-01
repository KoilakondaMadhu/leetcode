class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # Take the absolute values to simplify calculations
        d = abs(dividend)
        dv = abs(divisor)
        
        # Initialize the output variable to store the result
        output = 0

        # Perform integer division using subtraction and shifting
        while d >= dv:
            tmp = dv  # Temporary variable to store the current divisor
            mul = 1   # Multiplier for the current divisor

            # Subtract the current divisor from the dividend
            # and update the result and divisor for the next iteration
            while d >= tmp:
                d -= tmp
                output += mul
                mul += mul   # Double the multiplier
                tmp += tmp   # Double the divisor

        # Handle the sign of the result based on the signs of the original numbers
        if (dividend < 0 and divisor >= 0) or (divisor < 0 and dividend >= 0):
            output = -output

        # Ensure the result is within the 32-bit signed integer range
        return min(max(-2**31, output), 2**31 - 1)
