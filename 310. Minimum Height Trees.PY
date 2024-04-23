from collections import defaultdict, deque

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]  # Only one node, it's the root

        # Construct adjacency list
        adj_list = defaultdict(set)
        for u, v in edges:
            adj_list[u].add(v)
            adj_list[v].add(u)

        # Initialize leaves
        leaves = deque()
        for node in range(n):
            if len(adj_list[node]) == 1:
                leaves.append(node)

        # Continue removing leaves until 1 or 2 nodes left
        remaining_nodes = n
        while remaining_nodes > 2:
            num_leaves = len(leaves)
            remaining_nodes -= num_leaves
            for _ in range(num_leaves):
                leaf = leaves.popleft()
                neighbor = adj_list[leaf].pop()  # Remove the leaf's only neighbor
                adj_list[neighbor].remove(leaf)  # Remove the leaf from its neighbor's adjacency list
                if len(adj_list[neighbor]) == 1:
                    leaves.append(neighbor)

        # The remaining nodes in 'leaves' are the roots of MHTs
        return list(leaves)
