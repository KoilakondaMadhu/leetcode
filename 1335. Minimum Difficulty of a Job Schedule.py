class Solution:
    def minDifficulty(self, jobDifficulty, d):
        # Check if it's impossible to divide the jobs into d days
        if len(jobDifficulty) < d:
            return -1
        
        # Calculate the total sum of job difficulties
        total_sum = sum(jobDifficulty)
        
        # If there are no jobs, return 0 difficulty
        if total_sum == 0:
            return 0
        
        # Initialize memoization array
        memo = [[0] * len(jobDifficulty) for _ in range(d + 1)]
        
        # Call the helper function to compute the minimum difficulty
        self.helper(jobDifficulty, d, 0, memo)
        
        # The result is stored in memo[d][0]
        return memo[d][0]

    def helper(self, jd, daysLeft, idx, memo):
        # Get the length of the job difficulty array
        length = len(jd)
        
        # Check if the result for the current state is already memoized
        if memo[daysLeft][idx] != 0:
            return
        
        # Base case: if there is only one day left, compute and store the maximum difficulty
        if daysLeft == 1:
            num = max(jd[idx:])
            memo[daysLeft][idx] = num
            return
        
        # Initialize the maximum difficulty for the current cut
        max_difficulty = jd[idx]
        daysLeft -= 1
        stop = length - idx - daysLeft + 1
    
        # Initialize result to positive infinity
        res = float('inf')
        
        # Iterate through possible cuts
        for i in range(1, stop):
            # Update the maximum difficulty for the current cut
            max_difficulty = max(max_difficulty, jd[idx + i - 1])
            
            # Retrieve or compute the result for the remaining jobs after the cut
            other = memo[daysLeft][idx + i]
            if other == 0:
                self.helper(jd, daysLeft, idx + i, memo)
                other = memo[daysLeft][idx + i]
            
            # Update the result with the minimum difficulty found so far
            res = min(res, other + max_difficulty)   
        
        # Memoize the result for the current state
        memo[daysLeft + 1][idx] = res
