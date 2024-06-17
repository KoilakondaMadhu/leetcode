class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left = 0
        right = int(c**0.5)
        while left <= right:
            currentsum = left * left + right * right
            if currentsum == c:
                return True
            elif currentsum < c:
                left += 1
            else:
                right -= 1
        return False
    
