# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        return prev

# Helper function to create a linked list from a list of values (for testing)
def create_linked_list(values: list) -> Optional[ListNode]:
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for i in range(1, len(values)):
        current.next = ListNode(values[i])
        current = current.next
    return head

# Helper function to convert a linked list to a list of values (for testing)
def linked_list_to_list(head: Optional[ListNode]) -> list:
    output = []
    current = head
    while current:
        output.append(current.val)
        current = current.next
    return output

if __name__ == "__main__":
    # Example 1
    list1 = create_linked_list([1, 2, 3, 4, 5])
    solution = Solution()
    reversed_list1_head = solution.reverseList(list1)
    print(f"Original list 1: {linked_list_to_list(create_linked_list([1, 2, 3, 4, 5]))}")
    print(f"Reversed list 1: {linked_list_to_list(reversed_list1_head)}")

    # Example 2
    list2 = create_linked_list([1, 2])
    reversed_list2_head = solution.reverseList(list2)
    print(f"\nOriginal list 2: {linked_list_to_list(create_linked_list([1, 2]))}")
    print(f"Reversed list 2: {linked_list_to_list(reversed_list2_head)}")

    # Example 3 (empty list)
    list3 = create_linked_list([])
    reversed_list3_head = solution.reverseList(list3)
    print(f"\nOriginal list 3: {linked_list_to_list(create_linked_list([]))}")
    print(f"Reversed list 3: {linked_list_to_list(reversed_list3_head)}")

    # Example 4 (single node)
    list4 = create_linked_list([10])
    reversed_list4_head = solution.reverseList(list4)
    print(f"\nOriginal list 4: {linked_list_to_list(create_linked_list([10]))}")
    print(f"Reversed list 4: {linked_list_to_list(reversed_list4_head)}")
