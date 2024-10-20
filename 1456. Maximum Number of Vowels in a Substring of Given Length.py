class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        max_count = 0
        current_count = 0

        # Initialize the first window of size k
        for i in range(k):
            if s[i] in vowels:
                current_count += 1
        max_count = current_count

        # Slide the window across the string
        for i in range(k, len(s)):
            # Remove the element that goes out of the window
            if s[i - k] in vowels:
                current_count -= 1
            # Add the new element that enters the window
            if s[i] in vowels:
                current_count += 1
            
            # Update the maximum count if necessary
            max_count = max(max_count, current_count)

        return max_count
