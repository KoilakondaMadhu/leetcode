class Solution {
    public int maxDepth(String s) {
        int ans = 0; // Initialize a variable to store the maximum depth
        
        Stack<Character> st = new Stack<Character>(); // Create a stack to keep track of opening parentheses
        for (Character c : s.toCharArray()) { // Iterate through each character in the string
            if (c == '(') { // If the character is an opening parenthesis
                st.push(c); // Push it onto the stack
            } else if (c == ')') { // If the character is a closing parenthesis
                st.pop(); // Pop the corresponding opening parenthesis from the stack
            }
            
            ans = Math.max(ans, st.size()); // Update the maximum depth by taking the maximum of current maximum and the size of the stack
        }
        
        return ans; // Return the maximum depth
    }
}
