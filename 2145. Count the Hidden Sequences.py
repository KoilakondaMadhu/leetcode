class Solution:
    def numberOfArrays(self, diff: List[int], lower: int, upper: int) -> int:
        return max(0, upper-lower+1-max(accumulate(diff, initial=0))+min(accumulate(diff, initial=0)))
