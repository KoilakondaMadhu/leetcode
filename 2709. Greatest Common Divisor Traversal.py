class UnionFind:
    def __init__(self, n):
        # Initialize parent array where each element is its own parent
        self.par = [i for i in range(n)]
        # Initialize size array to keep track of the size of each component
        self.size = [1] * n
        # Initialize count to keep track of the number of components
        self.count = n
    
    def find(self, x):
        # Find operation with path compression
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]
    
    def union(self, x, y):
        # Union operation with union by rank
        px, py = self.find(x), self.find(y)
        if px == py:
            return
        if self.size[px] < self.size[py]:
            self.par[px] = py
            self.size[py] += self.size[px]
        else:
            self.par[py] = px
            self.size[px] += self.size[py]
        self.count -= 1

class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        # Initialize UnionFind data structure
        uf = UnionFind(len(nums))
        # Dictionary to store factor -> index of value mapping
        factor_index = {}
        
        # Loop through the nums list
        for i, n in enumerate(nums):
            f = 2
            # Find prime factors of current number
            while f * f <= n:
                if n % f == 0:
                    # If current factor exists in factor_index, union the indices
                    if f in factor_index:
                        uf.union(i, factor_index[f])
                    else:
                        factor_index[f] = i
                    # Continue dividing n by f until it's no longer divisible
                    while n % f == 0:
                        n = n // f
                f += 1
            # If there's any remaining factor > 1, process it
            if n > 1:
                if n in factor_index:
                    uf.union(i, factor_index[n])
                else:
                    factor_index[n] = i
        
        # If count is 1, all elements are connected
        return uf.count == 1
