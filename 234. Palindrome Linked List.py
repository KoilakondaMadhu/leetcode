# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # Initialize two pointers, fast and slow, both starting at the head of the linked list.
        fast = head
        slow = head
        
        # Move fast pointer twice as fast as slow pointer.
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        # Reverse the second half of the linked list.
        prev = None
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
            
        # Initialize two pointers, one starting from the head and the other starting from the reversed second half.
        left, right = head, prev
        
        # Compare elements from both halves.
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        
        return True
