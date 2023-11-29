class Solution:
    def hammingWeight(self, n: int) -> int:
        # Initialize a variable 'res' to store the count of '1' bits
        res = 0
        
        # Continue the loop until n becomes 0
        while n:
            # Increment 'res' by the value of the least significant bit of n
            res += n % 2
            
            # Right shift n by 1 bit, effectively removing the least significant bit
            n = n >> 1
        
        # Return the count of '1' bits
        return res



# Example 1:

# Input: n = 00000000000000000000000000001011
# Output: 3
# Explanation: The input binary string 00000000000000000000000000001011 has a total of three '1' bits.
# Example 2:

# Input: n = 00000000000000000000000010000000
# Output: 1
# Explanation: The input binary string 00000000000000000000000010000000 has a total of one '1' bit.
# Example 3:

# Input: n = 11111111111111111111111111111101
# Output: 31
# Explanation: The input binary string 11111111111111111111111111111101 has a total of thirty one '1' bits.
 

# Constraints:

# The input must be a binary string of length 32.
 
