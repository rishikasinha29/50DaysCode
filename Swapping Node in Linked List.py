from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k <= 0:
            return head

        # Find the kth node from the beginning
        current = head
        kth_from_start = None
        for _ in range(k - 1):
            if not current.next:
                return head  # k is out of bounds
            current = current.next
        kth_from_start = current

        # Find the kth node from the end using two pointers
        slow = head
        fast = head
        for _ in range(k - 1):
            fast = fast.next

        while fast.next:
            slow = slow.next
            fast = fast.next
        kth_from_end = slow

        # Swap the values of the two nodes
        if kth_from_start and kth_from_end:
            kth_from_start.val, kth_from_end.val = kth_from_end.val, kth_from_start.val

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
def print_linked_list(head: Optional[ListNode]) -> None:
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

# Example Usage:
if __name__ == "__main__":
    # Example 1
    head1 = create_linked_list([1, 2, 3, 4, 5])
    k1 = 2
    print("Original List 1:")
    print_linked_list(head1)
    swapped_head1 = Solution().swapNodes(head1, k1)
    print(f"List 1 after swapping {k1}th nodes:")
    print_linked_list(swapped_head1)
    print("-" * 20)

    # Example 2
    head2 = create_linked_list([7, 9, 6, 6, 7, 8, 3, 0, 9, 5])
    k2 = 5
    print("Original List 2:")
    print_linked_list(head2)
    swapped_head2 = Solution().swapNodes(head2, k2)
    print(f"List 2 after swapping {k2}th nodes:")
    print_linked_list(swapped_head2)
    print("-" * 20)

    # Example with k=1
    head3 = create_linked_list([10, 20, 30])
    k3 = 1
    print("Original List 3:")
    print_linked_list(head3)
    swapped_head3 = Solution().swapNodes(head3, k3)
    print(f"List 3 after swapping {k3}th nodes:")
    print_linked_list(swapped_head3)
    print("-" * 20)

    # Example where k is the last node
    head4 = create_linked_list([1, 2, 3, 4, 5])
    k4 = 5
    print("Original List 4:")
    print_linked_list(head4)
    swapped_head4 = Solution().swapNodes(head4, k4)
    print(f"List 4 after swapping {k4}th nodes:")
    print_linked_list(swapped_head4)
    print("-" * 20)

    # Example with k out of bounds
    head5 = create_linked_list([1, 2])
    k5 = 3
    print("Original List 5:")
    print_linked_list(head5)
    swapped_head5 = Solution().swapNodes(head5, k5)
    print(f"List 5 after swapping {k5}th nodes (k out of bounds):")
    print_linked_list(swapped_head5)
    print("-" * 20)
