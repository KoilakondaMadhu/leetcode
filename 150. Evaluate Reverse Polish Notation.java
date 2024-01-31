class Solution {
    public int evalRPN(String[] tokens) {
        // Create an array to act as a stack to store intermediate results
        int[] stack = new int[tokens.length];
        int top = 0; // Initialize the top of the stack

        // Iterate through each token in the input array
        for(String s : tokens) {
            char c = s.charAt(0); // Get the first character of the token

            // If the token is an operator ('+', '-', '*', '/'),
            // perform the corresponding operation on the operands.
            if(c == '+') {
                int b = stack[--top]; // Pop the top element (operand b)
                int a = stack[--top]; // Pop the second top element (operand a)
                stack[top++] = a + b; // Push the result of a + b onto the stack
            } else if(c == '-' && s.length() == 1) {
                int b = stack[--top];
                int a = stack[--top];
                stack[top++] = a - b;
            } else if(c == '*') {
                int b = stack[--top];
                int a = stack[--top];
                stack[top++] = a * b;
            } else if(c == '/') {
                int b = stack[--top];
                int a = stack[--top];
                stack[top++] = a / b;
            } else {
                // If the token is not an operator, it must be an operand.
                // Push the operand onto the stack after converting it to an integer.
                stack[top++] = Integer.parseInt(s);
            }
        }
        // After processing all tokens, the final result is on the top of the stack.
        return stack[0];
    }
}
