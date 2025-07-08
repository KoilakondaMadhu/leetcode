# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        key = root.val
        def search(root, key):
            if not root:
                return True
            return key == root.val and search(root.left, key) and search(root.right, key)
        
        return search(root, key)
