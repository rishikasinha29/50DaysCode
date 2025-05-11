import math

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        current = head
        while current and current.next:
            gcd_val = math.gcd(current.val, current.next.val)
            new_node = ListNode(gcd_val)
            new_node.next = current.next
            current.next = new_node
            current = current.next.next

        return head

# Helper function to create a linked list from a list of values
def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for i in range(1, len(values)):
        current.next = ListNode(values[i])
        current = current.next
    return head

# Helper function to print the linked list
def print_linked_list(head):
    elements = []
    current = head
    while current:
        elements.append(current.val)
        current = current.next
    print(elements)

# Example Usage:
if __name__ == "__main__":
    # Example 1
    head1 = create_linked_list([18, 6, 10, 3])
    print("Original Linked List 1:")
    print_linked_list(head1)
    solution = Solution()
    modified_head1 = solution.insertGreatestCommonDivisors(head1)
    print("Modified Linked List 1:")
    print_linked_list(modified_head1)

    print("-" * 20)

    # Example 2
    head2 = create_linked_list([7])
    print("Original Linked List 2:")
    print_linked_list(head2)
    modified_head2 = solution.insertGreatestCommonDivisors(head2)
    print("Modified Linked List 2:")
    print_linked_list(modified_head2)
