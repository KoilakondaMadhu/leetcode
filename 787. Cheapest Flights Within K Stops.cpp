class Solution {
public:
    int findCheapestPrice(int n, vector<vector<int>>& flights, int src, int dst, int k) {
        // Create an adjacency list to store the flights
        unordered_map<int, vector<pair<int, int>>> adj;
        
        // Populate the adjacency list using the flights vector
        for (auto& flight : flights) {
            adj[flight[0]].push_back({flight[1], flight[2]});
        }

        // Initialize a vector to store the distances from src to each node
        vector<int> dist(n, INT_MAX);
        dist[src] = 0;  // Distance from src to itself is 0

        // Create a queue for BFS traversal
        queue<pair<int, int>> q;
        q.push({src, 0});  // Push src node into the queue with distance 0
        int stops = 0;  // Variable to track the number of stops taken

        // Perform BFS traversal
        while (!q.empty() && stops <= k) {
            int sz = q.size();  // Number of nodes at current level
            while (sz-- > 0) {
                auto [node, distance] = q.front();  // Get the front node and its distance
                q.pop();  // Pop the node from the queue

                // If node has no outgoing flights, skip to the next node
                if (!adj.count(node)) continue;

                // Iterate over the neighbors of the current node
                for (auto& [neighbour, price] : adj[node]) {
                    // If the new price + current distance is not better than the current distance,
                    // skip to the next neighbor
                    if (price + distance >= dist[neighbour]) continue;
                    
                    // Update the distance to the neighbor and push it into the queue
                    dist[neighbour] = price + distance;
                    q.push({neighbour, dist[neighbour]});
                }
            }
            stops++;  // Increment the number of stops
        }
        
        // Return the distance to the destination node, or -1 if unreachable
        return dist[dst] == INT_MAX ? -1 : dist[dst];
    }
};
