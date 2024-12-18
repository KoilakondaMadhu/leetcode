class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, a, b):
        self.parent[self.find(b)] = self.find(a)

class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid)
        # Divide each square into 4 triangles
        uf = UnionFind(4 * n * n) 
        
        for row in range(n):
            for col in range(n):
                cell = grid[row][col]
                index = 4 * (row * n + col) 
                
                # When there are no lines in the square
                if cell == ' ':
                    uf.union(index+0, index+1)
                    uf.union(index+1, index+2)
                    uf.union(index+2, index+3)
                # When there's a bottom left - top right diagonal line dividing the square
                if cell == '/':
                    uf.union(index+0, index+3)
                    uf.union(index+1, index+2)
                # When there's a top left - bottom right diagonal line dividing the square
                if cell == '\\':
                    uf.union(index+2, index+3)
                    uf.union(index+0, index+1)
                # Connecting a square with square below it
                if row < n - 1:
                    uf.union(index+2, (index + 4*n) + 0)
                # Connecting a square with right side square
                if col < n - 1:
                    uf.union(index+1, (index + 4) + 3)
                    
        output = 0
        for i in range(4*n*n):
            if uf.find(i) == i:
                output += 1
        return output
