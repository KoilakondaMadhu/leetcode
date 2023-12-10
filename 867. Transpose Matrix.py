import numpy as np

class Solution:
    def transpose(self, A):
        # Convert the input list 'A' to a NumPy array
        nparr = np.array(A)
        
        # Use NumPy's transpose function to obtain the transpose of the array
        nparr = np.transpose(nparr)
        
        # Convert the NumPy array back to a nested list and return it
        return nparr.tolist()

# Example of how to use the Solution class
# Instantiate the Solution class
solution = Solution()

# Example input list
input_matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Call the transpose method with the example input
transposed_matrix = solution.transpose(input_matrix)

# Print the original and transposed matrices
print("Original Matrix:")
print(input_matrix)

print("\nTransposed Matrix:")
print(transposed_matrix)
