public class Solution {
    // Method to find the index of the first unique character in the input string
    public int firstUniqChar(String s) {
        // Array to store the frequency of each character (assuming only lowercase English letters)
        int freq[] = new int[26];
        
        // Count the frequency of each character in the string
        for (int i = 0; i < s.length(); i++)
            freq[s.charAt(i) - 'a']++; // Increment the frequency count at the corresponding index
        
        // Iterate through the string to find the first unique character
        for (int i = 0; i < s.length(); i++)
            if (freq[s.charAt(i) - 'a'] == 1) // If frequency is 1, it's the first unique character
                return i; // Return the index of the first unique character
        
        // If no unique character is found, return -1
        return -1;
    }
}
