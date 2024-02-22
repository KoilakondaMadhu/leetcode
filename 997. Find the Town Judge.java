class Solution {
    public int findJudge(int n, int[][] trust) {
        // Create an array to store the frequency of trust for each person
        int[] freq = new int[n+1];
        
        // Traverse through the 'trust' array
        for (int[] person: trust) {
            // Decrement the trust count for the person who trusts someone
            freq[person[0]]--;
            // Increment the trust count for the person who is trusted
            freq[person[1]]++;
        }
        
        // Check each person to find the one who is trusted by everyone else
        for (int i = 1; i <= n; ++i) {
            // If a person is trusted by everyone except themselves (n-1), they are the judge
            if (freq[i] == n - 1) return i;
        }
        
        // If no judge is found, return -1
        return -1;
    }
}
