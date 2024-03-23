class Solution:
    def reorderList(self, head):
        # Step 1: Find the middle of the list
        if not head: 
            return []  # If the list is empty, return []
        
        # Initialize slow and fast pointers to the head of the list
        slow, fast = head, head
        
        # Move slow one step at a time and fast two steps at a time
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        # At this point, slow is at the middle of the list
        
        # Step 2: Reverse the second half of the list
        prev, curr = None, slow.next
        while curr:
            nextt = curr.next  # Store the next node
            curr.next = prev    # Reverse the pointer
            prev = curr         # Move prev pointer forward
            curr = nextt        # Move curr pointer forward
        
        # At this point, prev is the new head of the reversed second half
        # and slow is at the end of the first half
        
        slow.next = None  # Break the link between the first and second halves
        
        # Step 3: Merge the two halves of the list
        head1, head2 = head, prev
        while head2:
            next_head1 = head1.next  # Store the next node from the first half
            next_head2 = head2.next  # Store the next node from the second half
            
            head1.next = head2  # Connect head1 to head2
            head2.next = next_head1  # Connect head2 to the next node of head1
            
            head1 = next_head1  # Move head1 forward
            head2 = next_head2  # Move head2 forward
