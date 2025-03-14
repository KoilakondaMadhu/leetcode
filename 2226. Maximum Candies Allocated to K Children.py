class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        lo, hi = 0, max(candies)+1
        def isValid(candyLimit):
            groupsCanBeFormed = 0
            for candy in candies:
                groupsCanBeFormed += (candy//candyLimit)
            return groupsCanBeFormed >= k
        while lo + 1 < hi:
            mid = lo + (hi -lo)//2
            if isValid(mid):
                lo = mid
            else:
                hi = mid
        return lo
