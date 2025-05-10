# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        """
        Removes the nth node from the end of a linked list and returns its head.

        Args:
            head: The head of the linked list.
            n: The position of the node to remove from the end (1-indexed).

        Returns:
            The head of the modified linked list.
        """
        # Create a dummy node to handle the case where the head needs to be removed.
        dummy = ListNode(0)
        dummy.next = head
        slow = dummy
        fast = dummy

        # Move the fast pointer n steps ahead.
        for _ in range(n):
            fast = fast.next

        # Move both pointers until the fast pointer reaches the end.
        # The slow pointer will be pointing to the node before the one to be removed.
        while fast.next:
            slow = slow.next
            fast = fast.next

        # Remove the nth node from the end.
        slow.next = slow.next.next

        return dummy.next
