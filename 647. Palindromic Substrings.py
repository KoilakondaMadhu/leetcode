class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        
        # Loop through each character in the string
        for i in range(len(s)):
            l = r = i  # Initialize left and right pointers for odd-length palindromes
            res += self.countPali(s, l, r)  # Count odd-length palindromes
            l = i  # Reset left pointer for even-length palindromes
            r = i + 1  # Reset right pointer for even-length palindromes
            res += self.countPali(s, l, r)  # Count even-length palindromes
            
        return res

    # Function to count palindromes with given left and right pointers
    def countPali(self, s, l, r):
        res = 0
        
        # Expand around the center and count palindromes
        while l >= 0 and r < len(s) and s[l] == s[r]:
            res += 1
            l -= 1
            r += 1
        
        return res
