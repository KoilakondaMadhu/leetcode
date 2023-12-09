public class Solution {

    // The method to perform inorder traversal and return the result as a list of integers
    public List<Integer> inorderTraversal(TreeNode root) {
        // List to store the result of inorder traversal
        List<Integer> res = new ArrayList<>();
        
        // Stack to keep track of the nodes during traversal
        Stack<TreeNode> stack = new Stack<>();
        
        // Start with the root of the tree
        TreeNode curr = root;

        // Continue the loop until we finish traversing the tree
        while (curr != null || !stack.isEmpty()) {
            // Traverse to the leftmost node of the current subtree and push nodes onto the stack
            while (curr != null) {
                stack.push(curr);
                curr = curr.left;
            }

            // Pop a node from the stack (it will be the leftmost node in the current subtree)
            curr = stack.pop();

            // Add the value of the popped node to the result list
            res.add(curr.val);

            // Move to the right subtree to continue the inorder traversal
            curr = curr.right;
        }

        // Return the final result list
        return res;
    }
}
