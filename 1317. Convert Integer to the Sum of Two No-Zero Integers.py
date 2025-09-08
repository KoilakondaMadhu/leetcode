class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        def has_no_zero(num):
            while num:
                if num % 10 == 0:
                    return False
                num //= 10
            return True
        for i in range(1, n):
            if has_no_zero(i) and has_no_zero(n - i):                
                return [i, n - i]
