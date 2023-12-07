class Solution:
    def largestOddNumber(self, num: str) -> str:
        # Iterate through the characters of the input string 'num' in reverse order.
        for i in range(len(num) - 1, -1, -1):
            # Check if the integer value of the current character is odd.
            if int(num[i]) % 2 != 0:
                # If the current character is odd, return the substring of 'num' from the beginning up to this character.
                return num[:i + 1]
        
        # If no odd digit is found in 'num', return an empty string.
        return ""
