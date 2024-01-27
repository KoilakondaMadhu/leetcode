import numpy as np

class Solution(object):
    def findPaths(self, m, n, N, i, j):
        paths = np.zeros((m, n), dtype=np.int64)
        paths[i][j] = 1
        out = 0
        mod = 10**9 + 7
        for _ in range(N):
            prev = paths % mod
            paths = prev - prev
            paths[1:] += prev[:-1]
            paths[:-1] += prev[1:]
            paths[:,1:] += prev[:,:-1]
            paths[:,:-1] += prev[:,1:]
            out += 4 * prev.sum() - paths.sum()
        return int(out % mod)
