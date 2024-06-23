class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        def parity(x):
            if x % 2 == 1:
                return 'odd'
            else:
                return 'even'
        for i in range(1,len(nums)):
            if parity(nums[i]) == parity(nums[i-1]):
                return False
        return True
