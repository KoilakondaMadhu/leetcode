from typing import List

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        # Step 1: Sort the greed factors and cookie sizes in ascending order
        g.sort()
        s.sort()
        
        # Initialize variables
        content_children = 0  # Number of satisfied children
        cookie_index = 0      # Index for iterating through cookies
        
        # Step 2: Iterate through cookies and greed factors
        while cookie_index < len(s) and content_children < len(g):
            # Step 3: Check if the current cookie size is sufficient for the current child's greed
            if s[cookie_index] >= g[content_children]:
                # If true, the child is satisfied, increment the count of content children
                content_children += 1
            
            # Move to the next cookie, regardless of whether the child was satisfied or not
            cookie_index += 1
        
        # Step 4: Return the total number of satisfied children
        return content_children
