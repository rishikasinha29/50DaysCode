class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        oddHead = head
        evenHead = head.next
        oddTail = oddHead
        evenTail = evenHead
        current = evenHead.next
        index = 3

        while current:
            if index % 2 != 0:  # Odd index
                oddTail.next = current
                oddTail = current
            else:  # Even index
                evenTail.next = current
                evenTail = current
            current = current.next
            index += 1

        oddTail.next = evenHead
        evenTail.next = None  # Ensure the even list terminates

        return oddHead

# Helper function to create a linked list from a list of values (for local testing)
def createLinkedList(values: list[int]) -> ListNode:
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for i in range(1, len(values)):
        current.next = ListNode(values[i])
        current = current.next
    return head

# Helper function to print a linked list (for local testing)
def printLinkedList(head: ListNode):
    elements = []
    current = head
    while current:
        elements.append(current.val)
        current = current.next
    print(elements)

# Example Usage (for local testing):
if __name__ == "__main__":
    list1 = createLinkedList([1, 2, 3, 4, 5])
    print("Original List 1:")
    printLinkedList(list1)
    solution = Solution()
    reorderedList1 = solution.oddEvenList(list1)
    print("Reordered List 1:")
    printLinkedList(reorderedList1)

    list2 = createLinkedList([2, 1, 3, 5, 6, 4, 7])
    print("\nOriginal List 2:")
    printLinkedList(list2)
    reorderedList2 = solution.oddEvenList(list2)
    print("Reordered List 2:")
    printLinkedList(reorderedList2)
