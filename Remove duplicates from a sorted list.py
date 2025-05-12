from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        dummy = ListNode(0)  # Use a dummy node to handle cases where the head needs to be removed
        dummy.next = head
        prev = dummy
        current = head

        while current:
            # Check if the current node has duplicates
            if current.next and current.val == current.next.val:
                # Skip all duplicate nodes
                while current.next and current.val == current.next.val:
                    current = current.next
                # Now current points to the last duplicate node, skip it as well
                prev.next = current.next
            else:
                # No duplicates, move both pointers forward
                prev = current
            current = current.next

        return dummy.next
