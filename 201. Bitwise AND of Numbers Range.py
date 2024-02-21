class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        # Initialize a variable to track the number of right shifts needed
        shift = 0
        
        # Continue looping until left and right become equal
        while left < right:
            # Right shift both left and right by 1
            left >>= 1
            right >>= 1
            
            # Increment the shift count
            shift += 1
        
        # Left shift left by the number of trailing zeroes up to the leftmost set bit
        # This will give the bitwise AND of all numbers in the range
        return left << shift
