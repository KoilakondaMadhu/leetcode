class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        min_time = 0

        for i in range(1, len(points)):
            x1, y1 = points[i - 1]
            x2, y2 = points[i]

            # Calculate horizontal and vertical distances
            horizontal_distance = abs(x2 - x1)
            vertical_distance = abs(y2 - y1)

            # Diagonal movement is more efficient
            diagonal_distance = min(horizontal_distance, vertical_distance)

            # Calculate remaining horizontal and vertical distances
            remaining_horizontal = horizontal_distance - diagonal_distance
            remaining_vertical = vertical_distance - diagonal_distance

            # Update the total minimum time
            min_time += diagonal_distance + max(remaining_horizontal, remaining_vertical)

        return min_time
