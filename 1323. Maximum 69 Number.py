class Solution:
    def maximum69Number(self, num: int) -> int:
        # Convert the integer to a string
        s = str(num)
        
        # Initialize index variable i to -1
        i = -1
        
        # Iterate through the string to find the first '6'
        for j in range(len(s)):
            if s[j] == '6':
                # Store the index of the first '6' found
                i = j
                break
        
        # If no '6' is found, return the original number
        if i == -1:
            return num
        else:
            # Replace the first '6' found with '9' and return the new integer
            return int(s[:i] + '9' + s[i + 1:])
