class Solution {
    public int subarraysDivByK(int[] nums, int k) {
        int n = nums.length; // Length of the input array
        int prefixMod = 0, result = 0; // Initialize prefixMod to 0 and result to 0
        int[] modGroups = new int[k]; // Array to store counts of prefix sums modulo k
        modGroups[0] = 1; // Initialize modGroups[0] to 1, to count the subarrays that are directly divisible by k

        for (int num : nums) { // Iterate through each number in the array
            // Calculate the current prefix sum modulo k
            // Adding k and taking modulo k again ensures the result is non-negative
            prefixMod = (prefixMod + num % k + k) % k;
            // Increment result by the count of previous prefix sums that have the same modulo k
            result += modGroups[prefixMod];
            // Increment the count of the current prefixMod in modGroups
            modGroups[prefixMod]++;
        }
        return result; // Return the total count of subarrays divisible by k
    }
}



// Example 1:

// Input: nums = [4,5,0,-2,-3,1], k = 5
// Output: 7
// Explanation: There are 7 subarrays with a sum divisible by k = 5:
// [4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]
// Example 2:

// Input: nums = [5], k = 9
// Output: 0
 
