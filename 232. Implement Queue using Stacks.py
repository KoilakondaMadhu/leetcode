class MyQueue:
    def __init__(self):
        # Initialize two stacks, s1 for main storage and s2 for temporary operations
        self.s1 = []
        self.s2 = []

    def push(self, x):
        # Push operation for a queue using two stacks
        
        # Move all elements from s1 to s2
        while self.s1:
            self.s2.append(self.s1.pop())
        
        # Add the new element to the bottom of s1
        self.s1.append(x)
        
        # Move all elements back from s2 to s1 to maintain FIFO order
        while self.s2:
            self.s1.append(self.s2.pop())

    def pop(self):
        # Pop operation for a queue using two stacks
        # Since elements are already in FIFO order, simply pop from s1
        return self.s1.pop()

    def peek(self):
        # Peek operation to view the front element of the queue
        # The front element of the queue is the top element of s1
        return self.s1[-1]

    def empty(self):
        # Check if the queue is empty
        # If s1 is empty, then the queue is empty
        return not self.s1
