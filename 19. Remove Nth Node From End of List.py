class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # Initialize two pointers, fast and slow, both pointing to the head of the linked list
        fast, slow = head, head
        
        # Move the fast pointer n steps ahead
        for _ in range(n):
            fast = fast.next
        
        # If fast pointer reaches the end of the list (None), remove the head node
        if not fast:
            return head.next
        
        # Move both fast and slow pointers until fast reaches the end of the list
        while fast.next:
            fast, slow = fast.next, slow.next
        
        # At this point, slow pointer is at the node just before the one to be removed
        # So, we skip the next node by updating the next pointer of slow
        slow.next = slow.next.next
        
        # Return the head of the modified linked list
        return head
