class Solution {
    public int[] sortedSquares(int[] A) {
        // Length of the input array
        int n = A.length;
        
        // Create an array to store the squared values, with the same length as A
        int[] result = new int[n];
        
        // Initialize two pointers i and j to the start and end of the array respectively
        int i = 0, j = n - 1;
        
        // Loop through the result array in reverse order
        for (int p = n - 1; p >= 0; p--) {
            // Compare the absolute values of the elements pointed by i and j
            if (Math.abs(A[i]) > Math.abs(A[j])) {
                // If the absolute value of A[i] is greater, square it and store in result
                result[p] = A[i] * A[i];
                // Move pointer i to the next element
                i++;
            } else {
                // If the absolute value of A[j] is greater, square it and store in result
                result[p] = A[j] * A[j];
                // Move pointer j to the previous element
                j--;
            }
        }
        // Return the result array containing squared values in non-decreasing order
        return result;
    }
}
