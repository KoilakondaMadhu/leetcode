class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # Remove trailing whitespaces from the string
        s = s.strip()
        
        # If the string is empty after removing whitespaces, return 0
        if not s:
            return 0
        
        # Split the string into words
        words = s.split()
        
        # Return the length of the last word
        return len(words[-1])

# Test cases
solution = Solution()
print(solution.lengthOfLastWord("Hello World"))  # Output: 5
print(solution.lengthOfLastWord("   fly me   to   the moon  "))  # Output: 4
print(solution.lengthOfLastWord("luffy is still joyboy"))  # Output: 6
