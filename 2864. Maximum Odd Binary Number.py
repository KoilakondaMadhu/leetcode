class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        # Initialize a variable to count the number of '1's
        count = 0
        
        # Iterate through each character in the input string
        for c in s:
            # If the character is '1', increment the count
            if c == "1":
                count += 1
        
        # Construct the modified binary number string
        # The number of '1's is count - 1, followed by len(s) - count '0's, and ending with '1'
        return (count - 1) * "1" + (len(s) - count) * "0" + "1"
