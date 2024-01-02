class Solution {
    // Function to find matrix of integers based on input array
    public List<List<Integer>> findMatrix(int[] nums) {
        // Create an array to store the frequency of each integer
        int freq[] = new int[nums.length + 1];

        // Create a list to store the resulting matrix
        ArrayList<List<Integer>> ans = new ArrayList<>();
        
        // Iterate through the input array
        for (int c : nums) {
            // Check if the current frequency is greater than or equal to the size of the result matrix
            if (freq[c] >= ans.size()) {
                // If true, add a new empty list to the result matrix
                ans.add(new ArrayList<>());
            }

            // Store the integer in the list corresponding to its current frequency.
            ans.get(freq[c]).add(c);
            
            // Increment the frequency count for the current integer
            freq[c]++;
        }

        // Return the resulting matrix
        return ans;
    }
}
