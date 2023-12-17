from collections import Counter
from typing import List

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        # Check for empty inputs
        if not s or not words:
            return []

        # Get the length of a single word and the total number of words
        word_len = len(words[0])
        word_count = len(words)
        total_len = word_len * word_count

        # Count the frequency of each word in the given list
        word_freq = Counter(words)

        # Initialize the result list to store starting indices of concatenated substrings
        result = []

        # Iterate over all possible starting indices for the concatenated substring
        for i in range(word_len):
            left, right = i, i
            current_freq = Counter()

            # Move the right pointer in increments of word length
            while right + word_len <= len(s):
                word = s[right:right + word_len]
                right += word_len
                current_freq[word] += 1

                # Adjust the window if the current word frequency exceeds the expected frequency
                while current_freq[word] > word_freq[word]:
                    left_word = s[left:left + word_len]
                    left += word_len
                    current_freq[left_word] -= 1

                # Check if the current window forms a concatenated substring
                if right - left == total_len:
                    result.append(left)

        # Return the list of starting indices
        return result
      
