from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs):
        # Initialize a defaultdict to store lists of anagrams
        anagram_map = defaultdict(list)
        
        # Iterate over each word in the input list
        for word in strs:
            # Sort the characters of the word and join them into a string
            sorted_word = ''.join(sorted(word))
            
            # Append the original word to the list associated with its sorted signature
            anagram_map[sorted_word].append(word)
        
        # Convert the values (lists of anagrams) in the anagram_map to a list and return
        return list(anagram_map.values())
