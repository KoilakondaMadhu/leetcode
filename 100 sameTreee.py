# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Check if both nodes are None, indicating they are equal
        if not p and not q:
            return True
        
        # Check if either node is None (but not both), indicating inequality
        if not p or not q or p.val != q.val:
            return False
        
        # Recursively check the left and right subtrees for equality
        return (self.isSameTree(p.left, q.left) and
                self.isSameTree(p.right, q.right))
