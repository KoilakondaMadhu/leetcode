class Solution {
    public String minWindow(String s, String t) {
        // Check for null or empty strings, or if s is shorter than t
        if (s == null || t == null || s.length() == 0 || t.length() == 0 ||
                s.length() < t.length()) {
            return new String();
        }
        
        // Initialize variables
        int[] map = new int[128]; // Map to store characters of string t
        int count = t.length();   // Count of characters in t
        int start = 0, end = 0;   // Pointers for sliding window
        int minLen = Integer.MAX_VALUE; // Minimum window length found
        int startIndex = 0;       // Starting index of minimum window
        
        // Fill map with characters from string t
        for (char c : t.toCharArray()) {
            map[c]++;
        }
        
        char[] chS = s.toCharArray(); // Convert string s to character array
        
        // Sliding window algorithm
        while (end < chS.length) {
            // If the character at 'end' is in t and hasn't been used up yet
            if (map[chS[end++]]-- > 0) {
                count--; // Decrement count
            }
            // When all characters of t are found in the window
            while (count == 0) {
                // Update minLen and startIndex if current window is smaller
                if (end - start < minLen) {
                    startIndex = start;
                    minLen = end - start;
                }
                // Move 'start' pointer to right, and update map and count
                if (map[chS[start++]]++ == 0) {
                    count++; // Increment count
                }
            }
        }

        // Return minimum window substring
        return minLen == Integer.MAX_VALUE ? new String() :
                new String(chS, startIndex, minLen);
    }
}
