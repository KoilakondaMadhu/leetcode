class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Check if the lengths of the strings are different
        if len(s) != len(t):
            return False

        # Create dictionaries to store character counts for each string
        counts, countt = {}, {}

        # Count occurrences of characters in the first string (s)
        for i in range(len(s)):
            counts[s[i]] = 1 + counts.get(s[i], 0)

        # Count occurrences of characters in the second string (t)
        for i in range(len(t)):
            countt[t[i]] = 1 + countt.get(t[i], 0)

        # Compare the character counts in both dictionaries
        for c in counts:
            if counts[c] != countt.get(c, 0):
                return False

        # If all character counts are equal, the strings are anagrams
        return True
