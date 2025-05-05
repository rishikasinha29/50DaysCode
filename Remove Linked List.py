class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        """
        Removes all nodes with a value equal to val from a linked list.

        Args:
            head (ListNode): The head of the linked list.
            val (int): The value to remove.

        Returns:
            ListNode: The new head of the modified linked list.
        """
        # Handle the case where the head node(s) need to be removed
        while head and head.val == val:
            head = head.next

        if not head:
            return None

        current = head
        while current.next:
            if current.next.val == val:
                current.next = current.next.next
            else:
                current = current.next

        return head

# Example Usage (for testing - you might not need this part in the online judge)
# Create a linked list: 1 -> 2 -> 6 -> 3 -> 4 -> 5 -> 6
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(6)
head.next.next.next = ListNode(3)
head.next.next.next.next = ListNode(4)
head.next.next.next.next.next = ListNode(5)
head.next.next.next.next.next.next = ListNode(6)

val_to_remove = 6
solution = Solution()
new_head = solution.removeElements(head, val_to_remove)

# Print the modified linked list
current = new_head
while current:
    print(current.val, end=" -> ")
    current = current.next
print("None")

# Example 2: Empty list
head2 = None
val_to_remove2 = 1
new_head2 = solution.removeElements(head2, val_to_remove2)
print("Empty list result:", new_head2)

# Example 3: All elements to be removed
head3 = ListNode(7)
head3.next = ListNode(7)
head3.next.next = ListNode(7)
val_to_remove3 = 7
new_head3 = solution.removeElements(head3, val_to_remove3)
print("All elements removed result:", new_head3)
