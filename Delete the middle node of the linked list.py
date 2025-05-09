from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        if not head.next:
            return None

        slow = head
        fast = head
        prev = None

        while fast and fast.next:
            fast = fast.next.next
            prev = slow
            slow = slow.next

        # slow is now pointing to the middle node
        if prev:
            prev.next = slow.next
        else:
            # This case happens when there are only two nodes,
            # and the first node is the middle one (index 0).
            # However, the initial checks handle single and empty lists.
            # For a list of two nodes, slow will be the second node,
            # and prev will be the first node.
            pass

        return head

# Helper function to create a linked list from a list of values
def create_linked_list(values: list[int]) -> Optional[ListNode]:
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for i in range(1, len(values)):
        current.next = ListNode(values[i])
        current = current.next
    return head

# Helper function to print a linked list
def print_linked_list(head: Optional[ListNode]):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

# Example Usage:
if __name__ == "__main__":
    # Example 1
    head1 = create_linked_list([1, 3, 4, 7, 1, 2, 6])
    print("Original List 1:")
    print_linked_list(head1)
    solution = Solution()
    new_head1 = solution.deleteMiddle(head1)
    print("List 1 after deleting middle node:")
    print_linked_list(new_head1)
    print("-" * 20)

    # Example 2
    head2 = create_linked_list([1, 2, 3, 4])
    print("Original List 2:")
    print_linked_list(head2)
    new_head2 = solution.deleteMiddle(head2)
    print("List 2 after deleting middle node:")
    print_linked_list(new_head2)
    print("-" * 20)

    # Example 3
    head3 = create_linked_list([2, 1])
    print("Original List 3:")
    print_linked_list(head3)
    new_head3 = solution.deleteMiddle(head3)
    print("List 3 after deleting middle node:")
    print_linked_list(new_head3)
    print("-" * 20)

    # Example with a single node
    head4 = create_linked_list([1])
    print("Original List 4:")
    print_linked_list(head4)
    new_head4 = solution.deleteMiddle(head4)
    print("List 4 after deleting middle node:")
    print_linked_list(new_head4)
    print("-" * 20)

    # Example with an empty list
    head5 = create_linked_list([])
    print("Original List 5:")
    print_linked_list(head5)
    new_head5 = solution.deleteMiddle(head5)
    print("List 5 after deleting middle node:")
    print_linked_list(new_head5)
    print("-" * 20)
