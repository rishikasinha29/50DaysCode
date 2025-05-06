from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None

        # 1. Find the length of the linked list
        length = 0
        current = head
        while current:
            length += 1
            current = current.next

        # 2. Handle the case where k is larger than the length
        k = k % length
        if k == 0:
            return head

        # 3. Find the (length - k)-th node from the beginning
        # This node will become the new tail
        slow = head
        fast = head
        for _ in range(k):
            fast = fast.next

        while fast.next:
            slow = slow.next
            fast = fast.next

        # 4. Perform the rotation
        new_head = slow.next
        slow.next = None  # Break the list at the new tail
        fast.next = head  # Connect the old tail to the old head

        return new_head

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
    elements = []
    current = head
    while current:
        elements.append(current.val)
        current = current.next
    print(elements)

# Example Usage:
if __name__ == "__main__":
    # Example 1
    head1 = create_linked_list([1, 2, 3, 4, 5])
    k1 = 2
    rotated_head1 = Solution().rotateRight(head1, k1)
    print("Original list 1:")
    print_linked_list(head1)
    print(f"Rotated list 1 by {k1}:")
    print_linked_list(rotated_head1)  # Output: [4, 5, 1, 2, 3]

    # Example 2
    head2 = create_linked_list([0, 1, 2])
    k2 = 4
    rotated_head2 = Solution().rotateRight(head2, k2)
    print("\nOriginal list 2:")
    print_linked_list(head2)
    print(f"Rotated list 2 by {k2}:")
    print_linked_list(rotated_head2)  # Output: [2, 0, 1]

    # Example with k = 0
    head3 = create_linked_list([10, 20])
    k3 = 0
    rotated_head3 = Solution().rotateRight(head3, k3)
    print("\nOriginal list 3:")
    print_linked_list(head3)
    print(f"Rotated list 3 by {k3}:")
    print_linked_list(rotated_head3)  # Output: [10, 20]

    # Example with k equal to length
    head4 = create_linked_list([7])
    k4 = 1
    rotated_head4 = Solution().rotateRight(head4, k4)
    print("\nOriginal list 4:")
    print_linked_list(head4)
    print(f"Rotated list 4 by {k4}:")
    print_linked_list(rotated_head4)  # Output: [7]

    # Example with empty list
    head5 = create_linked_list([])
    k5 = 5
    rotated_head5 = Solution().rotateRight(head5, k5)
    print("\nOriginal list 5:")
    print_linked_list(head5)
    print(f"Rotated list 5 by {k5}:")
    print_linked_list(rotated_head5)  # Output: []
