class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        len1, len2 = len(str1), len(str2)

        # Function to check if a given length is a common divisor
        def isdivisor(l):
            if len1 % l or len2 % l:
                return False
            f1, f2 = len1 // l, len2 // l
            return str1[:l] * f1 == str1 and str1[:l] * f1 == str2

        # Iterate over possible lengths of common divisors in descending order
        for l in range(min(len(str1), len(str2)), 0, -1):
            # Check if the current length is a common divisor
            if isdivisor(str1[:l]):
                # If it is, return the common divisor
                return str1[:l]

        # If no common divisor is found, return an empty string
        return ""


# For two strings s and t, we say "t divides s" if and only if s = t + ... + t (i.e., t is concatenated with itself one or more times).

# Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

 

# Example 1:

# Input: str1 = "ABCABC", str2 = "ABC"
# Output: "ABC"
# Example 2:

# Input: str1 = "ABABAB", str2 = "ABAB"
# Output: "AB"
# Example 3:

# Input: str1 = "LEET", str2 = "CODE"
# Output: ""
 

# Constraints:

# 1 <= str1.length, str2.length <= 1000
# str1 and str2 consist of English uppercase letters.
# Seen this question in a real interview before?
# 1/4
