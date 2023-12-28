class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        def dp(start, k):
            # Check if the subproblem has already been solved
            if (start, k) in memo:
                return memo[(start, k)]
            
            # Base cases
            if start == n or n - start <= k:
                return 0
            
            ans = sys.maxsize
            count = defaultdict(int)
            most_freq = 0
            
            # Iterate over the substring starting from 'start'
            for j in range(start, n):
                c = s[j]
                count[c] += 1
                most_freq = max(most_freq, count[c])
                
                # Calculate compressed length based on the most frequent character
                compressed_length = 1 + (len(str(most_freq)) if most_freq > 1 else 0)
                
                # Check if we can delete characters within the current window (j - start + 1)
                if k >= j - start + 1 - most_freq:
                    # Recur for the remaining substring after deleting characters
                    ans = min(ans, compressed_length + dp(j + 1, k - (j - start + 1 - most_freq)))
                
            # Memoize the result and return
            memo[(start, k)] = ans
            return ans
            
        # Length of the input string
        n = len(s)
        
        # Dictionary to memoize intermediate results
        memo = {}
        
        # Call the recursive function with initial parameters
        return dp(0, k)
