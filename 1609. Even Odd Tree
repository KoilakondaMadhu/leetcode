# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        # Initialize a variable to track whether the current level should have even or odd values
        even = True
        
        # Initialize a deque with the root node
        q = deque([root])
        
        # Iterate through the tree using BFS
        while q:
            # Initialize prev to track the previous value in the current level
            prev = float("-inf") if even else float("inf")
            
            # Iterate through all nodes in the current level
            for _ in range(len(q)):
                # Pop the leftmost node in the current level
                node = q.popleft()
                
                # Check conditions based on whether the level should have even or odd values
                if even and (node.val % 2 == 0 or node.val <= prev):
                    return False
                elif not even and (node.val % 2 == 1 or node.val >= prev):
                    return False
                
                # Enqueue the left and right children of the current node if they exist
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                
                # Update prev to the current node's value for the next iteration
                prev = node.val
            
            # Toggle even flag for the next level
            even = not even
        
        # If the entire tree satisfies the conditions, return True
        return True
