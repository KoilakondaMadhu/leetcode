from typing import List

class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        # Create an empty set to store the starting cities
        s = set()
        
        # Iterate through each path in the list of paths
        for i in paths:
            # Add the starting city of each path to the set
            s.add(i[0])
        
        # Iterate through each path in the list of paths again
        for i in paths:
            # Check if the destination city of the current path is not in the set of starting cities
            if i[1] not in s:
                # If not in the set, return the destination city as it is the destination without being a starting city
                return i[1]
