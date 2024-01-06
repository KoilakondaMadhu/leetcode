import java.util.Arrays;
import java.util.Comparator;

public class Solution {

    public int jobScheduling(int[] startTime, int[] endTime, int[] profit) {
        int numJobs = profit.length; // Number of jobs
        Job[] jobs = new Job[numJobs];

        // Create an array of Job objects to store information about each job
        for (int i = 0; i < numJobs; ++i) {
            jobs[i] = new Job(endTime[i], startTime[i], profit[i]);
        }

        // Sort the jobs array based on the end times of the jobs
        Arrays.sort(jobs, Comparator.comparingInt(job -> job.endTime));
        
        // Initialize an array to store the maximum profit at each position
        int[] dp = new int[numJobs + 1];

        // Iterate through each job
        for (int i = 0; i < numJobs; ++i) {
            int endTimeValue = jobs[i].endTime;
            int startTimeValue = jobs[i].startTime;
            int profitValue = jobs[i].profit;

            // Find the index of the latest non-conflicting job using binary search
            int latestNonConflictJobIndex = upperBound(jobs, i, startTimeValue);
            
            // Update the maximum profit at the current position
            dp[i + 1] = Math.max(dp[i], dp[latestNonConflictJobIndex] + profitValue);
        }

        // Return the maximum profit achievable by scheduling jobs
        return dp[numJobs];
    }

    // Binary search to find the index of the latest non-conflicting job
    private int upperBound(Job[] jobs, int endIndex, int targetTime) {
        int low = 0;
        int high = endIndex;

        while (low < high) {
            int mid = (low + high) / 2;
            if (jobs[mid].endTime <= targetTime) {
                low = mid + 1;
            } else {
                high = mid;
            }
        }

        return low;
    }

    // Inner class representing a Job with endTime, startTime, and profit
    private static class Job {
        int endTime;
        int startTime;
        int profit;

        public Job(int endTime, int startTime, int profit) {
            this.endTime = endTime;
            this.startTime = startTime;
            this.profit = profit;
        }
    }
}
