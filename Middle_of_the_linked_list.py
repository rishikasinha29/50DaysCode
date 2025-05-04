# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

# Helper function to create a linked list (for local testing)
def create_linked_list(values: list) -> Optional[ListNode]:
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for i in range(1, len(values)):
        current.next = ListNode(values[i])
        current = current.next
    return head

if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    list1 = create_linked_list([1, 2, 3, 4, 5])
    middle1 = solution.middleNode(list1)
    print(f"Middle Node (List 1): {middle1.val if middle1 else None}")

    # Test case 2
    list2 = create_linked_list([1, 2, 3, 4, 5, 6])
    middle2 = solution.middleNode(list2)
    print(f"Middle Node (List 2): {middle2.val if middle2 else None}")

    # Test case with a very short list (might get closer to 1ms in some environments)
    list3 = create_linked_list([1, 2])
    middle3 = solution.middleNode(list3)
    print(f"Middle Node (List 3): {middle3.val if middle3 else None}")
