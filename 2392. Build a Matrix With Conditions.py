class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        def determine_ordering(conditions):
            indegrees = [0 for i in range(k)]
            graph = {}

            for first,second in conditions:
                if first not in graph:
                    graph[first] = set()
                if second not in graph[first]:
                    graph[first].add(second)
                    indegrees[second-1]+=1 # account for 0 indexing
            
            queue = []
            top_order = []
            for i in range(len(indegrees)):
                if indegrees[i] == 0:
                    queue.append(i+1) # account for 0 indexing
                    top_order.append(i+1)
            
            while queue:
                node = queue.pop(0)
                
                if node in graph:
                    for neighbor in graph[node]:
                        indegrees[neighbor-1]-=1 # visit that neighbor
                        if indegrees[neighbor-1] == 0:
                            queue.append(neighbor)
                            top_order.append(neighbor)

            final_indegrees = sum(indegrees)
            cycle = False
            if final_indegrees > 0:
                cycle = True
            
            return cycle, top_order
        
        cycle1, row_order = determine_ordering(rowConditions)
        cycle2, col_order = determine_ordering(colConditions)
        if cycle1 or cycle2:
            return []
        
        final_coords = [[-1,-1] for i in range(k)]

        for i in range(len(row_order)):
            val = row_order[i]
            final_coords[val-1][0] = i
        
        for i in range(len(col_order)):
            val = col_order[i]
            final_coords[val-1][1] = i
        
        output = [[0 for i in range(k)] for j in range(k)]

        for index, coord in enumerate(final_coords):
            output[coord[0]][coord[1]] = index+1
        
        return output

