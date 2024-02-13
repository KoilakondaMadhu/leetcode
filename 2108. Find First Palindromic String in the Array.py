class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        # Iterate through each word in the list
        for w in words:
            # Initialize left and right pointers for each word
            l, r = 0, len(w) - 1
            
            # While characters at left and right pointers are equal
            while w[l] == w[r]:
                # If left pointer has crossed or is equal to the right pointer,
                # it means the word is a palindrome
                if l >= r:
                    return w
                
                # Move left pointer to the right and right pointer to the left
                l += 1
                r -= 1
            
        # If no palindrome is found, return an empty string
        return ""
