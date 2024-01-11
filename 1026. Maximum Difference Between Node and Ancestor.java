class Solution {
    // Main function to find the maximum difference
    public int maxAncestorDiff(TreeNode root) {
        if (root == null)
            return 0;

        // Call the helper function to perform the calculation
        return diff(root)[2];
    }

    // Helper function to calculate the minimum value, maximum value, and global maximum difference
    public int[] diff(TreeNode root) {
        // Base case: if the node is null, return an array with extreme values and 0 difference
        if (root == null)
            return new int[]{Integer.MAX_VALUE, Integer.MIN_VALUE, 0};

        // Recursively calculate the values for the left and right subtrees
        int[] left = diff(root.left);
        int[] right = diff(root.right);

        // Update the minimum and maximum values for the current subtree
        int min = Math.min(root.val, Math.min(left[0], right[0]));
        int max = Math.max(root.val, Math.max(left[1], right[1]));

        // Calculate the local difference for the current node
        int localDiff = Math.max(Math.abs(root.val - min), Math.abs(root.val - max));

        // Calculate the global maximum difference considering the left and right subtrees
        int globalDiff = Math.max(Math.max(left[2], right[2]), localDiff);

        // Return an array with updated min, max, and global difference values
        return new int[]{min, max, globalDiff};
    }
}
