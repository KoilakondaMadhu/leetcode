class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_to_t = {}  # Mapping from characters in s to characters in t
        t_to_s = {}  # Mapping from characters in t to characters in s
        
        for i in range(len(s)):
            if s[i] in s_to_t:
                # If the character in s is already mapped to a different character in t
                if s_to_t[s[i]] != t[i]:
                    return False
            else:
                # Create a new mapping for the character in s
                s_to_t[s[i]] = t[i]
                
            if t[i] in t_to_s:
                # If the character in t is already mapped to a different character in s
                if t_to_s[t[i]] != s[i]:
                    return False
            else:
                # Create a new mapping for the character in t
                t_to_s[t[i]] = s[i]
        
        return True
