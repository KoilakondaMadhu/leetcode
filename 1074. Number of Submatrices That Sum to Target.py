def numSubmatrixSumTarget(self, matrix, target):
    m, n = len(matrix), len(matrix[0])  # Get dimensions of the matrix

    # Preprocess the matrix to store cumulative sums for each row
    for row in range(m):
        for col in range(1, n):
            matrix[row][col] += matrix[row][col - 1]

    count = 0  # Initialize count variable to store the number of submatrices

    # Iterate through all possible pairs of column indices
    for c1 in range(n):
        for c2 in range(c1, n):
            prefix_sum_count = {0: 1}  # Store prefix sums and their counts
            sum_val = 0  # Initialize the sum of elements in the current submatrix

            # Iterate through each row to calculate the sum of elements in the submatrix
            for row in range(m):
                sum_val += matrix[row][c2] - (matrix[row][c1 - 1] if c1 > 0 else 0)
                count += prefix_sum_count.get(sum_val - target, 0)  # Check if there is a submatrix with the target sum
                prefix_sum_count[sum_val] = prefix_sum_count.get(sum_val, 0) + 1  # Update the prefix sum count

    return count  # Return the total count of submatrices with the target sum
