class Solution {
    int result = 0;
    int[] digits;

    public int pseudoPalindromicPaths(TreeNode root) {
        digits = new int[10];
        dfs(root);
        return result;
    }

    void dfs(TreeNode root) {
        if (root == null) {
            return;
        }
        digits[root.val]++;
        if (root.left == null && root.right == null) {
            if (isPalindrome()) {
                result++;
            }
        } else {
            dfs(root.left);
            dfs(root.right);
        }
        digits[root.val]--;
    }

    boolean isPalindrome() {
        int odd = 0;
        for (int i = 1; i <= 9; i++) {
            if (digits[i] % 2 != 0) {
                odd++;
            }
        }
        return odd <= 1;
    }
}
