# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        # Define a recursive depth-first search (DFS) function
        def dfs(node):
            # Base case: If the current node is None, return 0
            if not node:
                return 0
            
            # Initialize current_val to 0
            current_val = 0
            
            # Check if the value of the current node is within the specified range [low, high]
            if low <= node.val <= high:
                # If yes, set current_val to the value of the current node
                current_val = node.val
            
            # Recursively call dfs on the left subtree and right subtree
            left_sum = dfs(node.left)
            right_sum = dfs(node.right)
            
            # Return the sum of current_val, left subtree sum, and right subtree sum
            return current_val + left_sum + right_sum
        
        # Start the DFS from the root of the binary search tree
        return dfs(root)
