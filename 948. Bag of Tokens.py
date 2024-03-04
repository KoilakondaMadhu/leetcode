class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        # Sort the tokens array in ascending order
        tokens.sort()
        # Initialize pointers for the leftmost and rightmost elements of the sorted array
        left, right = 0, len(tokens) - 1
        # Initialize variables to keep track of the current score and maximum score achieved
        score = max_score = 0
        
        # Loop until the left pointer exceeds the right pointer
        while left <= right:
            # If we have enough power to play the current token face-up
            if power >= tokens[left]:
                # Play the token face-up, update power and score
                power -= tokens[left]
                left += 1
                score += 1
                # Update the maximum score if needed
                max_score = max(max_score, score)
            # If we have a positive score and cannot play the current token face-up
            elif score > 0:
                # Play the token face-down, update power and score
                power += tokens[right]
                right -= 1
                score -= 1
            # If we cannot play the current token face-up and have a score of 0
            else:
                # Break the loop as we cannot proceed further
                break
                
        # Return the maximum score achieved
        return max_score
