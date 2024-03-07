class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        # Check if the linked list is empty
        if not head:
            return False
        
        # Initialize two pointers, slow and fast, both starting at the head
        slow = head
        fast = head.next
        
        # Traverse the linked list until slow and fast meet
        while slow != fast:
            # If fast reaches the end of the list (or beyond), it means there is no cycle
            if not fast or not fast.next:
                return False
            
            # Move slow one step forward
            slow = slow.next
            
            # Move fast two steps forward
            fast = fast.next.next
        
        # If slow and fast meet, it means there is a cycle in the linked list
        return True
