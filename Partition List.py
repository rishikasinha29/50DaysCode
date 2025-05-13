from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        # Create dummy nodes for the two partitions
        less_head = ListNode(0)
        greater_equal_head = ListNode(0)
        less_tail = less_head
        greater_equal_tail = greater_equal_head

        # Iterate through the original list
        current = head
        while current:
            if current.val < x:
                less_tail.next = current
                less_tail = current
            else:
                greater_equal_tail.next = current
                greater_equal_tail = current
            current = current.next

        # Concatenate the two lists
        less_tail.next = greater_equal_head.next
        greater_equal_tail.next = None  # Ensure the greater/equal partition ends properly

        return less_head.next
