from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        # Initialize a deque (double-ended queue) with the root node
        q = deque([root])
        
        # While the queue is not empty
        while q:
            # Pop the leftmost node from the queue
            node = q.popleft()
            
            # If the popped node has a right child, add it to the queue
            if node.right:
                q.append(node.right)
            
            # If the popped node has a left child, add it to the queue
            if node.left:
                q.append(node.left)
        
        # At this point, the last node processed from the queue is the leftmost leaf node
        # which corresponds to the bottom left value in the binary tree
        return node.val
