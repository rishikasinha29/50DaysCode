class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        """
        Merges two sorted linked lists into one sorted linked list by splicing the nodes.

        Args:
            list1: The head of the first sorted linked list.
            list2: The head of the second sorted linked list.

        Returns:
            The head of the merged sorted linked list.
        """
        # Handle empty list cases
        if not list1:
            return list2
        if not list2:
            return list1

        # Determine the head of the merged list
        if list1.val <= list2.val:
            merged_head = list1
            list1 = list1.next
        else:
            merged_head = list2
            list2 = list2.next

        current = merged_head

        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        # Append the remaining nodes of the non-empty list
        if list1:
            current.next = list1
        elif list2:
            current.next = list2

        return merged_head

# Helper function to create a linked list (this can stay outside the class if you prefer)
def create_linked_list(values: list[int]) -> ListNode | None:
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for i in range(1, len(values)):
        current.next = ListNode(values[i])
        current = current.next
    return head

# Helper function to convert a linked list to a list (can also stay outside)
def linked_list_to_list(head: ListNode | None) -> list[int]:
    output = []
    current = head
    while current:
        output.append(current.val)
        current = current.next
    return output

# Example usage (this is likely in your '_driver' or main part of the script)
if __name__ == "__main__":
    list1_values = [1, 2, 4]
    list2_values = [1, 3, 4]
    list1_head = create_linked_list(list1_values)
    list2_head = create_linked_list(list2_values)
    sol = Solution()  # Create an instance of the Solution class
    merged_head = sol.mergeTwoLists(list1_head, list2_head)
    print(linked_list_to_list(merged_head))
