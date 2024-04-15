# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        # Helper function to perform DFS
        def dfs(node, path_sum):
            if not node:
                return 0
            # Calculate the current path sum
            path_sum = path_sum * 10 + node.val
            # If the current node is a leaf, return the path sum
            if not node.left and not node.right:
                return path_sum
            # Otherwise, continue DFS traversal
            return dfs(node.left, path_sum) + dfs(node.right, path_sum)
        
        # Start DFS traversal from the root with initial path sum 0
        return dfs(root, 0)

# Example usage:
# Construct the binary tree from the given input
root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(3)

root2 = TreeNode(4)
root2.left = TreeNode(9)
root2.right = TreeNode(0)
root2.left.left = TreeNode(5)
root2.left.right = TreeNode(1)

# Create an instance of the Solution class
sol = Solution()
# Test the sumNumbers function with the given examples
print(sol.sumNumbers(root1))  # Output: 25
print(sol.sumNumbers(root2))  # Output: 1026
