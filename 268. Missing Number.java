class Solution {
    public int missingNumber(int[] nums) {
        // Calculate the expected sum of numbers from 0 to n using the formula n*(n+1)/2
        int n = nums.length;
        int sum = n * (n + 1) / 2;
        
        // Iterate through the array and subtract each number from the sum
        for (int i : nums) {
            sum -= i;
        }
        
        // The remaining sum will be the missing number
        return sum;
    }
}
