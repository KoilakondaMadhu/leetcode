class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        removed = 0
        
        for digit in num:
            while stack and removed < k and stack[-1] > digit:
                stack.pop()
                removed += 1
            stack.append(digit)
        
        # If there are remaining digits to be removed, remove them from the end of the stack
        while removed < k:
            stack.pop()
            removed += 1
        
        # Construct the result string while removing leading zeroes
        result = ''.join(stack).lstrip('0')
        
        # If the result is empty, return '0'
        if not result:
            return '0'
        else:
            return result
