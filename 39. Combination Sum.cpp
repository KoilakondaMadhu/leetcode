#include <vector>

class Solution {
public:
    // Recursive helper function to find combinations
    void helper(vector<vector<int>> &res, vector<int> &cd, vector<int> &nums, int t, int sum, int idx) {
        // Base case: combination sum equals target
        if (sum == t) {
            res.push_back(nums); // Valid combination found, add to result
            return;
        }
        
        // Base case: sum exceeds target or reached end of candidates
        if (sum > t || idx == cd.size()) {
            return;
        }

        // Include the current candidate in the combination
        nums.push_back(cd[idx]);
        helper(res, cd, nums, t, sum + cd[idx], idx);

        // Backtrack by excluding the current candidate
        nums.pop_back();
        helper(res, cd, nums, t, sum, idx + 1);
    }

    // Main function to initiate the recursive process
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        vector<vector<int>> res; // Result vector to store combinations
        vector<int> nums; // Current combination vector
        helper(res, candidates, nums, target, 0, 0); // Call the helper function
        return res; // Return the final result
    }
};
