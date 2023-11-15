# Given a 0-indexed string s, permute s to get a new string t such that:

# All consonants remain in their original places. More formally, if there is an index i with 0 <= i < s.length such that s[i] is a consonant, then t[i] = s[i].
# The vowels must be sorted in the nondecreasing order of their ASCII values. More formally, for pairs of indices i, j with 0 <= i < j < s.length such that s[i] and s[j] are vowels, then t[i] must not have a higher ASCII value than t[j].
# Return the resulting string.

# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in lowercase or uppercase. Consonants comprise all letters that are not vowels.

 class Solution:
    def sortVowels(self, s: str) -> str:
        # Step 1: Collect vowels and sort them in descending order
        vowels_sorted = sorted([c for c in s if c.lower() in 'aeiou'], reverse=True)

        # Step 2: Construct the answer string by replacing vowels in sorted order
        result = []
        for char in s:
            if char.lower() in 'aeiou':
                # Replace vowel with the next vowel from the sorted list
                result.append(vowels_sorted.pop())
            else:
                # Keep non-vowel characters unchanged
                result.append(char)

        # Step 3: Join the characters to form the final string
        return ''.join(result)

# Case 1
# Case 2
# Input
# s =
# "lEetcOde"
# Output
# "lEOtcede"
# Expected
# "lEOtcede"

# Input
# s =
# "lYmpH"
# Output
# "lYmpH"
# Expected
# "lYmpH"

# Explanation:

# Step 1 (Line 4): Collect vowels and sort them in descending order.

# python
# Copy code
# vowels_sorted = sorted([c for c in s if c.lower() in 'aeiou'], reverse=True)
# vowels_sorted is a list containing the vowels from the input string s, sorted in descending order.
# Step 2 (Lines 7-12): Construct the answer string by replacing vowels with the sorted vowels.

# python
# Copy code
# result = []
# for char in s:
#     if char.lower() in 'aeiou':
#         # Replace vowel with the next vowel from the sorted list
#         result.append(vowels_sorted.pop())
#     else:
#         # Keep non-vowel characters unchanged
#         result.append(char)
# Iterate through each character in the input string s.
# If the character is a vowel, replace it with the next vowel from the sorted list (vowels_sorted).
# If the character is not a vowel, keep it unchanged.
# Step 3 (Line 15): Join the characters to form the final string.

# python
# Copy code
# return ''.join(result)
# Convert the list of characters (result) into a string by joining them together.
# The overall goal is to sort the vowels in the input string while maintaining the order of non-vowel characters. The sorted vowels are replaced back into the original string, resulting in the final sorted string.
