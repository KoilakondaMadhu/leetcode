class Solution {
    public int minimumOneBitOperations(int n) {
        // Base case: If n is 0, no operations are needed.
        if (n == 0) {
            return 0;
        }
        
        // Initialize variables k and curr.
        int k = 0;   // k represents the position of the most significant bit.
        int curr = 1; // curr represents the value of the most significant bit.

        // Find the most significant bit and its position.
        while (curr * 2 <= n) {
            curr *= 2;
            k++;
        }

        // Calculate the result using bitwise operations.
        // 1 << (k + 1) is equivalent to 2^(k + 1).
        // Subtracting 1 creates a mask with k+1 bits set to 1.
        // XOR with n flips the bits of n up to the most significant bit.
        // Finally, recursively call the function for the remaining bits.
        return (1 << (k + 1)) - 1 - minimumOneBitOperations(n ^ curr);
    }
}
