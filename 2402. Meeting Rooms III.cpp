#include <vector>
#include <algorithm>
#include <climits>

using namespace std;

class Solution {
public:
    int mostBooked(int n, vector<vector<int>>& meetings) {
        // Initialize vectors to track room availability time and meeting counts for each room
        vector<long long> roomAvailabilityTime(n, 0);
        vector<int> meetingCount(n, 0);
        
        // Sort meetings by start time
        sort(meetings.begin(), meetings.end());

        for (auto& meeting : meetings) {
            int start = meeting[0], end = meeting[1];
            long long minRoomAvailabilityTime = LLONG_MAX;
            int minAvailableTimeRoom = 0;
            bool foundUnusedRoom = false;

            // Check each room's availability
            for (int i = 0; i < n; i++) {
                // If the room is available at the meeting start time
                if (roomAvailabilityTime[i] <= start) {
                    foundUnusedRoom = true;
                    meetingCount[i]++;  // Increment meeting count for the room
                    roomAvailabilityTime[i] = end;  // Update room availability time
                    break;
                }

                // Find the room with the minimum availability time
                if (minRoomAvailabilityTime > roomAvailabilityTime[i]) {
                    minRoomAvailabilityTime = roomAvailabilityTime[i];
                    minAvailableTimeRoom = i;
                }
            }

            // If no unused room is found, allocate the room with the minimum availability time
            if (!foundUnusedRoom) {
                roomAvailabilityTime[minAvailableTimeRoom] += end - start;
                meetingCount[minAvailableTimeRoom]++;
            }
        }
        
        // Find the room with the maximum meeting count
        int maxMeetingCount = 0, maxMeetingCountRoom = 0;
        for (int i = 0; i < n; i++) {
            if (meetingCount[i] > maxMeetingCount) {
                maxMeetingCount = meetingCount[i];
                maxMeetingCountRoom = i;
            }
        }
        
        // Return the index of the room with the maximum meeting count
        return maxMeetingCountRoom;
    }
};
