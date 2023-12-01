class Solution:
    def trailingZeroes(self, n: int) -> int:
        # Initialize the count of trailing zeroes
        count = 0
        
        # Keep dividing n by 5 and update the count
        while n >= 5:
            n //= 5
            count += n
        
        return count
# Trailing zeroes in the factorial result from the multiplication of factors of 2 and 5. Since factors of 2 are usually more abundant, counting factors of 5 is sufficient to determine the number of trailing zeroes.
# The loop continuously divides n by 5 and accumulates the count of factors of 5. This effectively counts the number of trailing zeroes in the factorial of n.
# The result is returned as the final count.
