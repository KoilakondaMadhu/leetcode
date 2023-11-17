class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = ""  # Initialize an empty string to store the merged result
        remainder = ""  # Initialize an empty string to store any remaining characters

        # Check if the length of word1 is less than the length of word2
        if len(word1) < len(word2):
            remainder = word2[len(word1):]  # Store the remaining characters of word2
        # Check if the length of word2 is less than the length of word1
        elif len(word2) < len(word1):
            remainder = word1[len(word2):]  # Store the remaining characters of word1

        # Iterate over the smaller of the two word lengths
        for i in range(min(len(word1), len(word2))):
            ans += word1[i]  # Append character from word1 to the result string
            ans += word2[i]  # Append character from word2 to the result string

        # Append any remaining characters (from the longer word) to the result string
        ans += remainder

        return ans  # Return the merged result
