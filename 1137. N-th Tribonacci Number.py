class Solution:
    def tribonacci(self, n: int) -> int:
        # Initialize an array to store Tribonacci numbers
        A = [0]*(n+1)
        
        # Base cases
        if n == 0 or n == 1:
            return n
        if n == 2:
            return 1
        
        # Initial Tribonacci numbers
        A[0] = 0
        A[1] = 1
        A[2] = 1
        
        # Fill the array with Tribonacci numbers
        for i in range(3, n+1):
            A[i] = A[i-1] + A[i-2] + A[i-3]
        
        # Return the nth Tribonacci number
        return A[n]
