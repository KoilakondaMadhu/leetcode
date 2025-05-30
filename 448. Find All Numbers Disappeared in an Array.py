class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        right = set(range(1,len(nums)+1))
        res = list(right - set(nums))
        return res
