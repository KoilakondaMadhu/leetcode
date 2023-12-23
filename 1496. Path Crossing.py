class Solution:
    def isPathCrossing(self, path: str) -> bool:
        # Define possible movements in the form of (dx, dy)
        moves = {
            "N": (0, 1),
            "S": (0, -1),
            "W": (-1, 0),
            "E": (1, 0)
        }

        # Set to keep track of visited coordinates
        visited = {(0, 0)}

        # Initialize starting coordinates
        x = 0
        y = 0

        # Iterate through each character in the path
        for c in path:
            # Retrieve the corresponding movement for the current character
            dx, dy = moves[c]

            # Update the current coordinates based on the movement
            x += dx
            y += dy

            # Check if the current coordinates have been visited before
            if (x, y) in visited:
                # If visited, the path has crossed itself
                return True

            # Add the current coordinates to the set of visited coordinates
            visited.add((x, y))

        # If the loop completes without any crossing, return False
        return False
