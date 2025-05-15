class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteNode(self, node: ListNode):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next

# Helper function to create a linked list for testing
def create_linked_list(elements):
    if not elements:
        return None
    head = ListNode(elements[0])
    current = head
    for i in range(1, len(elements)):
        current.next = ListNode(elements[i])
        current = current.next
    return head

# Helper function to print a linked list for testing
def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

if __name__ == '__main__':
    solver = Solution()

    # Example 1
    head1 = create_linked_list([4, 5, 1, 9])
    node_to_delete1 = head1.next  # The node with value 5
    print("Original linked list 1:")
    print_linked_list(head1)
    solver.deleteNode(node_to_delete1)
    print("Linked list 1 after deletion:")
    print_linked_list(head1)
    print("-" * 20)

    # Example 2
    head2 = create_linked_list([4, 5, 1, 9])
    # To get the node with value 1, we traverse the list
    current = head2
    node_to_delete2 = None
    while current:
        if current.val == 1:
            node_to_delete2 = current
            break
        current = current.next

    print("Original linked list 2:")
    print_linked_list(head2)
    if node_to_delete2:
        solver.deleteNode(node_to_delete2)
        print("Linked list 2 after deletion:")
        print_linked_list(head2)
    else:
        print("Node with value 1 not found in the second list.")
    print("-" * 20)

    # Example with a different list
    head3 = create_linked_list([1, 2, 3, 4, 5])
    node_to_delete3 = head3.next.next  # The node with value 3
    print("Original linked list 3:")
    print_linked_list(head3)
    solver.deleteNode(node_to_delete3)
    print("Linked list 3 after deletion:")
    print_linked_list(head3)
