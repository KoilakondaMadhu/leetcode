# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import Dict, Set
from collections import deque

class Solution:
    def amountOfTime(self, root: TreeNode, start: int) -> int:
        # Dictionary to store the adjacency list representation of the tree
        tree_map: Dict[int, Set[int]] = {}
        
        # Build the adjacency list using the convert function
        self.convert(root, 0, tree_map)
        
        # Breadth-first search to find the time taken to reach all nodes from the start node
        queue = deque([start])
        minute = 0
        visited = {start}

        while queue:
            level_size = len(queue)
            while level_size > 0:
                current = queue.popleft()
                
                # Explore neighbors and add them to the queue if not visited
                for num in tree_map[current]:
                    if num not in visited:
                        visited.add(num)
                        queue.append(num)
                
                level_size -= 1
            minute += 1

        # Return the total time taken (subtracting 1 to exclude the starting point)
        return minute - 1

    def convert(self, current: TreeNode, parent: int, tree_map: Dict[int, Set[int]]):
        # Recursive function to build the adjacency list representation of the tree
        if current is None:
            return
        if current.val not in tree_map:
            tree_map[current.val] = set()
        adjacent_list = tree_map[current.val]
        
        # Add parent and children to the adjacency list
        if parent != 0:
            adjacent_list.add(parent)
        if current.left:
            adjacent_list.add(current.left.val)
        if current.right:
            adjacent_list.add(current.right.val)
        
        # Recursive calls for left and right subtrees
        self.convert(current.left, current.val, tree_map)
        self.convert(current.right, current.val, tree_map)
