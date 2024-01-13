class Solution:
    def minSteps(self, s: str, t: str) -> int:
        # Initialize arrays to store the frequency of characters in s and t
        freq_s = [0] * 26
        freq_t = [0] * 26

        # Count the frequency of characters in s
        for char in s:
            freq_s[ord(char) - ord('a')] += 1

        # Count the frequency of characters in t
        for char in t:
            freq_t[ord(char) - ord('a')] += 1

        # Initialize the answer to 0
        steps = 0

        # Loop over all characters
        for i in range(26):
            # If the frequency of a character in t is less than in s,
            # add the difference to the answer
            steps += max(0, freq_s[i] - freq_t[i])

        return steps
