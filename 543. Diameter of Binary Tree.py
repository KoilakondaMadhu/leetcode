# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Initialize a list to store the result (maximum diameter found)
        res = [0]
        
        # Define a depth-first search (DFS) function to calculate the diameter
        def dfs(root):
            # Base case: If the current node is None, return -1 (representing depth of empty subtree)
            if not root:
                return -1
            
            # Recursively calculate the depth of the left subtree
            left = dfs(root.left)
            
            # Recursively calculate the depth of the right subtree
            right = dfs(root.right)
            
            # Update the maximum diameter found so far
            res[0] = max(res[0], 2 + left + right)
            
            # Return the depth of the current node in the tree
            return 1 + max(left, right)
        
        # Call the depth-first search function with the root node to start traversal
        dfs(root)
        
        # Return the maximum diameter found
        return res[0]
