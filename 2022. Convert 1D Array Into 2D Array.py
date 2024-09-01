class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        return ([], [*zip(*[iter(original)]*n)])[m*n == len(original)]


