# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def replaceValueInTree(self, root: TreeNode) -> TreeNode:
        def dfs(nodes):
            if not nodes:
                return

            # Calculate total sum of child nodes at the current level
            total_sum = 0
            for node in nodes:
                if node.left:
                    total_sum += node.left.val
                if node.right:
                    total_sum += node.right.val

            # Create an array for the next level of child nodes
            child_nodes = []
            for node in nodes:
                cur_sum = 0
                if node.left:
                    cur_sum += node.left.val
                if node.right:
                    cur_sum += node.right.val

                # Update child node values
                if node.left:
                    node.left.val = total_sum - cur_sum
                    child_nodes.append(node.left)
                if node.right:
                    node.right.val = total_sum - cur_sum
                    child_nodes.append(node.right)

            # Recur for the next level
            dfs(child_nodes)

        # Initialize root value to 0 and start DFS
        if root:
            root.val = 0
            dfs([root])

        return root
