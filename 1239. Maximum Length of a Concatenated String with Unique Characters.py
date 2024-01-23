class Solution:
    def maxLength(self, arr: List[str]) -> int:
        # Initialize an array to store the bitwise representation of strings without duplicates
        dp = [0]
        # Initialize the result variable to store the maximum length
        res = 0
        
        # Iterate through each string in the input array
        for s in arr:
            # Initialize variables for the bitwise representation of characters and duplicates
            a, dup = 0, 0
            
            # Check for duplicate characters in the current string
            for c in s:
                dup |= a & (1 << (ord(c) - ord('a')))
                a |= 1 << (ord(c) - ord('a'))
            
            # If there are duplicates, skip to the next string
            if dup > 0:
                continue
            
            # Iterate through the existing dp array in reverse order
            for i in range(len(dp) - 1, -1, -1):
                # If the bitwise AND operation is non-zero, there are common characters, so skip
                if (dp[i] & a) > 0:
                    continue
                
                # Append the new bitwise representation to the dp array
                dp.append(dp[i] | a)
                # Update the result with the maximum length of the combined strings
                res = max(res, bin(dp[i] | a).count('1'))
        
        # Return the final result
        return res
