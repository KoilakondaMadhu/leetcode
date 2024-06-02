class Solution {
    public void reverseString(char[] s) {
        // Initialize two pointers, one starting from the beginning of the array (i)
        // and the other starting from the end of the array (j).
        int i = 0;
        int j = s.length - 1;
        
        // Loop until the two pointers meet or cross each other.
        while (i <= j) {
            // Swap the elements at the i-th and j-th positions.
            char temp = s[i];
            s[i] = s[j];
            s[j] = temp;
            // Move the first pointer to the right.
            i++;
            // Move the second pointer to the left.
            j--;
        }
    }
}
