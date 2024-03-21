class Solution {
    // Method to reverse a singly linked list
    public ListNode reverseList(ListNode head) {
        // Base case: if the head is null or there's only one node, return head
        if (head == null || head.next == null) {
            return head;
        }
        // Recursively reverse the rest of the list and get the new head of the reversed list
        ListNode reversedListHead = reverseList(head.next);
        // Adjust pointers to reverse the current node
        head.next.next = head; // Make the next node point back to the current node
        head.next = null; // Break the link from the current node to its next node
        // Return the new head of the reversed list
        return reversedListHead;
    }
}
