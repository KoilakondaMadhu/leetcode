public class Solution {
    public int maxFrequencyElements(int[] nums) {
        // Find the frequency of each element
        Map<Integer, Integer> frequencies = new HashMap<>();
        for (int num : nums) {
            frequencies.put(num, frequencies.getOrDefault(num, 0) + 1); // Increment the frequency of the current number
        }

        // Determine the maximum frequency
        int maxFrequency = 0;
        for (int frequency : frequencies.values()) {
            maxFrequency = Math.max(maxFrequency, frequency); // Update maxFrequency with the maximum frequency found so far
        }

        // Calculate the total frequencies of elements with the maximum frequency
        int frequencyOfMaxFrequency = 0;
        for (int frequency : frequencies.values()) {
            if (frequency == maxFrequency) {
                frequencyOfMaxFrequency++; // Increment frequencyOfMaxFrequency for each element with maximum frequency
            }
        }
        
        // Return the product of frequencyOfMaxFrequency and maxFrequency
        return frequencyOfMaxFrequency * maxFrequency;
    }
}
