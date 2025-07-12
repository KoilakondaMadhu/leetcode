class Solution:
    def earliestAndLatest(self, n: int, firstPlayer: int, secondPlayer: int) -> List[int]:
        @lru_cache(None)
        def dp(l, r, k):
            if l == r:  return (1, 1)
            if l > r:   return dp(r, l, k)
            a, b = inf, -inf
            for i in range(1, l + 1):
                for j in range(l - i + 1, r - i + 1):
                    s = i + j
                    if l + r - k // 2 <= s <= (k + 1) // 2:
                        x, y = dp(i, j, (k + 1) // 2)
                        if x + 1 < a: a = x + 1
                        if y + 1 > b: b = y + 1
            return (a, b)

        return list(dp(firstPlayer, n - secondPlayer + 1, n))
