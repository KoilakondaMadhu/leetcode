class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # Check if n is not zero and if the bitwise AND of n and n - 1 is zero
        # If n is a power of two, n & (n - 1) will result in 0 because a power of two in binary
        # has only one bit set and subtracting 1 from it flips all bits to the right of the only set bit
        # For example, 8 in binary is 1000, and 8 - 1 = 7 in binary is 0111
        # Performing a bitwise AND operation on 1000 and 0111 results in 0000
        return n and not(n & n - 1)
