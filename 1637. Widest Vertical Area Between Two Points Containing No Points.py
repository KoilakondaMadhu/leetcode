import java.util.Arrays;

public class Solution {
    public int maxWidthOfVerticalArea(int[][] points) {
        // Sort the points based on their x-coordinates using a custom comparator
        Arrays.sort(points, (a, b) -> Integer.compare(a[0], b[0]));
        
        // Initialize a variable to store the maximum width
        int ans = 0;
        
        // Iterate through the sorted points
        for (int i = 1; i < points.length; i++) {
            // Calculate the width between consecutive x-coordinates
            int width = points[i][0] - points[i - 1][0];
            
            // Update the maximum width if the current width is greater
            ans = Math.max(ans, width);
        }
        
        // Return the maximum width of the vertical area
        return ans;
    }
}
