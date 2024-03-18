import java.util.Arrays;

class Solution {
    public int findMinArrowShots(int[][] points) {
        // Sorting the points based on their end coordinates in ascending order
        Arrays.sort(points, (a, b) -> Integer.compare(a[1], b[1]));
        
        // Initializing the number of arrows required to 1
        int arrow = 1;
        
        // Initializing the end coordinate of the first balloon
        int end = points[0][1];
        
        // Iterating through the sorted array of points
        for (int i = 1; i < points.length; i++) {
            // If the start coordinate of the current balloon is greater than the current end coordinate,
            // it means a new arrow is required
            if (points[i][0] > end) {
                arrow++; // Incrementing the arrow count
                end = points[i][1]; // Updating the end coordinate to the end of the current balloon
            }
        }
        
        // Returning the minimum number of arrows required
        return arrow;
    }
}
