class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True

        # Find the middle of the linked list using the fast and slow pointer approach
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse the second half of the linked list
        second_half = self.reverseList(slow)

        # Compare the first half and the reversed second half
        first_half = head
        while second_half:
            if first_half.val != second_half.val:
                return False
            first_half = first_half.next
            second_half = second_half.next

        return True

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev

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

# Example Usage:
if __name__ == "__main__":
    # Example 1
    list1 = create_linked_list([1, 2, 2, 1])
    solution = Solution()
    print(f"Is [1, 2, 2, 1] a palindrome? {solution.isPalindrome(list1)}")

    # Example 2
    list2 = create_linked_list([1, 2])
    print(f"Is [1, 2] a palindrome? {solution.isPalindrome(list2)}")

    # Example 3
    list3 = create_linked_list([])
    print(f"Is [] a palindrome? {solution.isPalindrome(list3)}")

    # Example 4
    list4 = create_linked_list([5])
    print(f"Is [5] a palindrome? {solution.isPalindrome(list4)}")

    # Example 5
    list5 = create_linked_list([1, 2, 3, 2, 1])
    print(f"Is [1, 2, 3, 2, 1] a palindrome? {solution.isPalindrome(list5)}")
