class Solution:
    def minOperations(self, a: str) -> int:
        # Initialize counters for two possible operations
        s, s1 = 0, 0
        
        # Iterate through the characters of the input string
        for i in range(len(a)):
            # If the index is even
            if i % 2 == 0:
                # If the current character is "0", increment s1
                if a[i] == "0":
                    s1 += 1
                # If the current character is "1", increment s
                else:
                    s += 1
            # If the index is odd
            else:
                # If the current character is "1", increment s1
                if a[i] == "1":
                    s1 += 1
                # If the current character is "0", increment s
                else:
                    s += 1
        
        # Return the minimum of s and s1, representing the minimum operations
        return min(s, s1)
