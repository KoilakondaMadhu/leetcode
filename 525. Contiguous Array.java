import java.util.Arrays;

class Solution {
    public int findMaxLength(int[] nums) {
        // Initialize an array to keep track of cumulative counts
        // We use 2 * nums.length + 1 to accommodate both positive and negative indices
        int[] arr = new int[2 * nums.length + 1];
        
        // Fill the array with -2 to indicate that no count has been encountered yet
        Arrays.fill(arr, -2);
        
        // Set the initial count at the middle of the array
        arr[nums.length] = -1;
        
        // Initialize variables to keep track of maximum length and current count
        int maxlen = 0;
        int count = 0;
        
        // Iterate through the input array
        for (int i = 0; i < nums.length; i++) {
            // Update the count based on the value of the current element
            count = count + (nums[i] == 0 ? -1 : 1);
            
            // Check if the current count has been encountered before
            if (arr[count + nums.length] >= -1) {
                // If yes, update maxlen if the current subarray is longer
                maxlen = Math.max(maxlen, i - arr[count + nums.length]);
            } else {
                // If not, update the array with the current index
                arr[count + nums.length] = i;
            }
        }
        
        // Return the maximum length of a contiguous subarray with equal 0s and 1s
        return maxlen;
    }
}
