# 1930. Unique Length-3 Palindromic Subsequences



class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        # Create a set to store unique letters in the string
        letters = set(s)
        # Initialize the count of palindromic subsequences
        ans = 0
        
        # Iterate over each unique letter in the set
        for letter in letters:
            # Find the first and last occurrence indices of the current letter
            i, j = s.index(letter), s.rindex(letter)
            # Initialize a set to store characters between the first and last occurrences
            between = set()
            
            # Iterate over characters between the first and last occurrences
            for k in range(i + 1, j):
                # Add characters to the set
                between.add(s[k])
            
            # Update the count by adding the length of the set 'between'
            ans += len(between)

        # Return the total count of palindromic subsequences
        return ans


# -> Hint
# Given a string s, return the number of unique palindromes of length three that are a subsequence of s.
# -----------------------------------------------------------------------------------------------------------------
# Note that even if there are multiple ways to obtain the same subsequence, it is still only counted once.

# A palindrome is a string that reads the same forwards and backwards.

# A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

# For example, "ace" is a subsequence of "abcde".
 

# Example 1:

# Input: s = "aabca"
# Output: 3
# Explanation: The 3 palindromic subsequences of length 3 are:
# - "aba" (subsequence of "aabca")
# - "aaa" (subsequence of "aabca")
# - "aca" (subsequence of "aabca")
# Example 2:

# Input: s = "adc"
# Output: 0
# Explanation: There are no palindromic subsequences of length 3 in "adc".
# Example 3:

# Input: s = "bbcbaba"
# Output: 4
# Explanation: The 4 palindromic subsequences of length 3 are:
# - "bbb" (subsequence of "bbcbaba")
# - "bcb" (subsequence of "bbcbaba")
# - "bab" (subsequence of "bbcbaba")
# - "aba" (subsequence of "bbcbaba")
 

# Constraints:

# 3 <= s.length <= 105
# s consists of only lowercase English letters.
# Seen this question in a real interview before?
# 1/4
# Yes
# No

# _________________
# Topics_______ __|
# Hash Table      |
# String          |
# Prefix Sum      |
# ________________|
# Companies
# Hint 1
# What is the maximum number of length-3 palindromic strings?
# Hint 2
# How can we keep track of the characters that appeared to the left of a given position?
# Similar Questions
# Count Palindromic Subsequences
