import java.util.PriorityQueue;

public class Solution {
    public int furthestBuilding(int[] heights, int bricks, int ladders) {
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        
        for (int i = 0; i < heights.length - 1; i++) {
            int diff = heights[i + 1] - heights[i];
            
            if (diff > 0) {
                pq.add(diff);
                
                // If the number of heights in the priority queue exceeds the number of ladders available,
                // use a ladder if available, otherwise use bricks
                if (pq.size() > ladders) {
                    bricks -= pq.poll();
                    
                    // If bricks are negative, it means we cannot proceed further
                    if (bricks < 0) {
                        return i;
                    }
                }
            }
        }
        
        // If we reach here, it means we can reach the end of the buildings
        return heights.length - 1;
    }
}
