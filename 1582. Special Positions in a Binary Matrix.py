from typing import List

class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        # Initialize a variable to store the count of special elements
        ans = 0
        
        # Get the number of rows and columns in the matrix
        m = len(mat)
        n = len(mat[0])
        
        # Iterate through each element in the matrix
        for row in range(m):
            for col in range(n):
                # Check if the current element is 1 (special element)
                if mat[row][col] == 0:
                    continue  # Skip to the next element if the current element is 0
                
                # Initialize a flag to check if the current element is special
                good = True
                
                # Check the entire column for the current element
                for r in range(m):
                    if r != row and mat[r][col] == 1:
                        good = False
                        break
                
                # Check the entire row for the current element
                for c in range(n):
                    if c != col and mat[row][c] == 1:
                        good = False
                        break
                
                # If the current element is special, increment the count
                if good:
                    ans += 1
        
        # Return the total count of special elements
        return ans
