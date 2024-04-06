class Solution {
    public String minRemoveToMakeValid(String s) {
        // Create a StringBuilder initialized with the input string
        StringBuilder sb = new StringBuilder(s);
        
        // Initialize a stack to keep track of indices of opening parentheses
        Stack<Integer> st = new Stack<>();
        
        // Iterate through each character of the string
        for (int i = 0; i < sb.length(); ++i) {
            // If an opening parenthesis is encountered, push its index onto the stack
            if (sb.charAt(i) == '(')
                st.add(i);
            // If a closing parenthesis is encountered
            if (sb.charAt(i) == ')') {
                // If there's a matching opening parenthesis in the stack, pop its index
                if (!st.empty())
                    st.pop();
                // If there's no matching opening parenthesis, mark this closing parenthesis for removal
                else
                    sb.setCharAt(i, '*');
            }
        }
        
        // Handle remaining unmatched opening parentheses by marking them for removal
        while (!st.empty())
            sb.setCharAt(st.pop(), '*');
        
        // Remove all marked characters and return the modified string
        return sb.toString().replaceAll("\\*", "");
    }
}
