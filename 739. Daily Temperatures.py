class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Initialize a list to store the result
        res = [0] * len(temperatures)
        
        # Initialize a stack to store index-value pairs
        stack = []  # Each element of the stack is a tuple: (index, value)

        # Iterate through the temperatures in reverse order
        for i in range(len(temperatures) - 1, -1, -1):
            # While the stack is not empty and the current temperature is greater
            # than or equal to the temperature at the top of the stack,
            # pop elements from the stack
            while stack and temperatures[i] >= stack[-1][1]:
                stack.pop()

            # If there are elements remaining in the stack,
            # calculate the difference between the current index and the index
            # at the top of the stack and store it in the result
            if stack:
                res[i] = stack[-1][0] - i

            # Push the current index and temperature onto the stack
            stack.append((i, temperatures[i]))
        
        # Return the result
        return res
