class Solution {
    public TreeNode addOneRow(TreeNode root, int val, int depth) {
        // Check if the depth is 1
        if (depth == 1) {
            TreeNode node = new TreeNode(val);
            node.left = root;
            return node;
        }
        // Call the insert method to add nodes at the specified depth
        insert(root, depth, val, 1);
        return root;
    }
    
    // Recursive method to insert nodes at the specified depth
    public void insert(TreeNode node, int d, int v, int currentDepth) {
        if (node == null) return;
        
        // If we have reached the depth - 1, add nodes at the current node
        if (currentDepth == d - 1) {
            TreeNode tempLeft = node.left; // Store the current left child
            node.left = new TreeNode(v);   // Create a new left child with the given value
            node.left.left = tempLeft;     // Set the original left child as the left child of the new left child
            
            TreeNode tempRight = node.right; // Store the current right child
            node.right = new TreeNode(v);    // Create a new right child with the given value
            node.right.right = tempRight;    // Set the original right child as the right child of the new right child
        } else {
            // Continue traversing the tree
            insert(node.left, d, v, currentDepth + 1);
            insert(node.right, d, v, currentDepth + 1);
        }
    } 
}
