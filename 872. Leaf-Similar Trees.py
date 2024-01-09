class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        # Define a function to collect leaf values of a tree and store them in a list
        def collect_leaf_values(root, leaf_values):
            # Base case: if the current node is None, return
            if not root:
                return
            # Check if the current node is a leaf (both left and right children are None)
            if not root.left and not root.right:
                # If it's a leaf, append its value to the list
                leaf_values.append(root.val)
            # Recursively call the function for left and right subtrees
            collect_leaf_values(root.left, leaf_values)
            collect_leaf_values(root.right, leaf_values)

        # Initialize empty lists to store leaf values of each tree
        leaf_values1 = []
        leaf_values2 = []

        # Collect leaf values for the first tree (root1)
        collect_leaf_values(root1, leaf_values1)

        # Collect leaf values for the second tree (root2)
        collect_leaf_values(root2, leaf_values2)

        # Check if the collected leaf values for both trees are equal
        return leaf_values1 == leaf_values2
