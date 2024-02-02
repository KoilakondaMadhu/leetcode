from collections import deque  # Import deque from collections module

class Solution:
    def sequentialDigits(self, low, high):
        out = []  # Initialize an empty list to store the sequential digits
        queue = deque(range(1, 10))  # Create a deque containing digits from 1 to 9
        while queue:  # Continue the loop until the queue is empty
            elem = queue.popleft()  # Remove and return the leftmost element from the queue
            if low <= elem <= high:  # Check if the element is within the specified range
                out.append(elem)  # Append the element to the output list if it satisfies the condition
            last = elem % 10  # Get the last digit of the current element
            if last < 9:  # Check if the last digit is less than 9
                queue.append(elem * 10 + last + 1)  # Add the next sequential number to the queue
        return out  # Return the list of sequential digits within the specified range
