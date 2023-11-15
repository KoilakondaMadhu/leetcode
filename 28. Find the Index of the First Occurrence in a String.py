# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

 

# Example 1:

# Input: haystack = "sadbutsad", needle = "sad"
# Output: 0
# Explanation: "sad" occurs at index 0 and 6.
# The first occurrence is at index 0, so we return 0.
# Example 2:

# Input: haystack = "leetcode", needle = "leeto"
# Output: -1
# Explanation: "leeto" did not occur in "leetcode", so we return -1.
 

# Constraints:

# 1 <= haystack.length, needle.length <= 104
# # haystack and needle consist of only lowercase English characters







class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # Step 1: Initialize the Longest Prefix Suffix (LPS) array with zeros
        lps = [0] * len(needle)

        # Step 2: Preprocessing - Build the LPS array
        pre = 0
        for i in range(1, len(needle)):
            # Compare characters at positions i and pre in the needle
            while pre > 0 and needle[i] != needle[pre]:
                # If a mismatch occurs, update pre based on LPS array
                pre = lps[pre-1]
            # If there is a match, update pre and LPS array
            if needle[pre] == needle[i]:
                pre += 1
                lps[i] = pre

        # Step 3: Main algorithm - Search for needle in haystack
        n = 0  # Initialize needle index
        for h in range(len(haystack)):
            # Check for mismatches and update needle index
            while n > 0 and needle[n] != haystack[h]:
                n = lps[n-1]
            # If there is a match, update needle index
            if needle[n] == haystack[h]:
                n += 1
            # If the entire needle is found, return the starting index
            if n == len(needle):
                return h - n + 1

        # If no match is found, return -1
        return -1
