class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        a = len(nums1)
        b = len(nums2)
        c = 0
        d = 0
        if a % 2 != 0:
            for i in nums2:
                d ^= i
        if b % 2 != 0:
            for i in nums1:
                c ^= i
        return c ^ d
