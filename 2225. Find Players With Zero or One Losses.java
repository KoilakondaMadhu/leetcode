class Solution {
    public List<List<Integer>> findWinners(int[][] matches) {
        // Initialize an array to keep track of losses for each participant
        int[] losses = new int[100001];

        // Process each match
        for (int i = 0; i < matches.length; i++) {
            // Get the participants of the current match
            int win = matches[i][0];
            int loss = matches[i][1];

            // If the winner has no losses recorded, mark as a potential winner
            if (losses[win] == 0) {
                losses[win] = -1; // -1 indicates a potential winner
            } 

            // If the loser has a win recorded, mark as having lost
            if (losses[loss] == -1) {
                losses[loss] = 1; // 1 indicates a loss
            } else {
                losses[loss]++; // Increment the count of losses
            }
        }

        // Create lists to store participants with zero and one loss
        List<Integer> zeroLoss = new ArrayList<>();
        List<Integer> oneLoss = new ArrayList<>();

        // Separate participants based on their losses
        for (int i = 0; i < losses.length; i++) {
            if (losses[i] == -1) {
                zeroLoss.add(i); // Participants with zero losses (potential winners)
            } else if (losses[i] == 1) {
                oneLoss.add(i); // Participants with exactly one loss
            }
        }

        // Create a list of lists to store the results
        List<List<Integer>> result = new ArrayList<>();
        result.add(zeroLoss); // Add the list of potential winners
        result.add(oneLoss);  // Add the list of participants with one loss

        return result;
    }
}
