class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def backtrack(row, col, index):
            # Base case: If all characters of the word have been found
            if index == len(word):
                return True
            
            # Check if current cell is out of bounds or doesn't match the current character
            if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]) or board[row][col] != word[index]:
                return False
            
            # Temporarily mark the current cell as visited
            temp = board[row][col]
            board[row][col] = '#'
            
            # Explore neighboring cells recursively
            found = backtrack(row + 1, col, index + 1) or \
                    backtrack(row - 1, col, index + 1) or \
                    backtrack(row, col + 1, index + 1) or \
                    backtrack(row, col - 1, index + 1)
            
            # Backtrack: Restore the original value of the cell
            board[row][col] = temp
            
            return found
        
        # Iterate through each cell of the board
        for i in range(len(board)):
            for j in range(len(board[0])):
                if backtrack(i, j, 0): # Start exploring from current cell
                    return True
        
        return False
