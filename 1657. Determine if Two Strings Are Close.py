class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        # Check if lengths are equal
        if len(word1) != len(word2):
            return False

        # Count frequencies of characters in both words
        count1 = Counter(word1)
        count2 = Counter(word2)

        # Check if sets of characters are the same
        if set(count1.keys()) != set(count2.keys()):
            return False

        # Sort frequency counts and check if they are the same
        return sorted(count1.values()) == sorted(count2.values())
