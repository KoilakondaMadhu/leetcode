from collections import defaultdict

class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        # Initialize a set to store people with secrets
        secrets = set([0, firstPerson]) # Initially, include person 0 and the firstPerson
        
        # Dictionary to map time to adjacency list of meetings
        time_map = {} # key: time, value: adjacency list of meetings
        
        # Populate the time_map dictionary
        for src, dst, t in meetings:
            if t not in time_map:
                time_map[t] = defaultdict(list)
            time_map[t][src].append(dst)
            time_map[t][dst].append(src)
            
        # Depth-first search (DFS) function to explore the connected components
        def dfs(src, adj):
            if src in visit:
                return
            visit.add(src)
            secrets.add(src) # Add the current person to the set of people with secrets
            for nei in adj[src]:
                dfs(nei, adj)
        
        # Iterate through the time_map keys in sorted order
        for t in sorted(time_map.keys()):
            visit = set() # Initialize a set to keep track of visited nodes for each time t
            for src in time_map[t]:
                if src in secrets: # If the current source node is already in the set of people with secrets
                    dfs(src, time_map[t]) # Perform DFS from this source node within the current time t
                    
        return list(secrets) # Return the list of people with secrets
