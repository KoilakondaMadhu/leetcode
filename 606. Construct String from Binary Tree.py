# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        # Initialize an empty list to store the result
        res = []
        
        # Define a helper function for preorder traversal
        def preorder(node):
            # If the node is None, return and exit the current call
            if not node:
                return 
            
            # Append an opening parenthesis to the result
            res.append("(")
            
            # Append the value of the current node to the result
            res.append(str(node.val))
            
            # If the node has no left child but has a right child, append empty parentheses
            if not node.left and node.right:
                res.append("()")
            
            # Recursively call the function for the left and right children
            preorder(node.left)
            preorder(node.right)
            
            # Append a closing parenthesis to the result
            res.append(")")
        
        # Start the preorder traversal from the root
        preorder(root)
        
        # Join the elements in the result list into a string,
        # and remove the leading and trailing parentheses
        return "".join(res)[1:-1]
