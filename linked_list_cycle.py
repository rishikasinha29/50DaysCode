class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head or not head.next:
            return False

        slow = head
        fast = head.next

        while slow != fast:
            if not fast or not fast.next:
                return False
            slow = slow.next
            fast = fast.next.next

        return True

# Example Usage (for testing purposes - not part of the solution)
if __name__ == '__main__':
    # Example 1: Cycle present
    head1 = ListNode(3)
    node2 = ListNode(2)
    node0 = ListNode(0)
    node_minus_4 = ListNode(-4)
    head1.next = node2
    node2.next = node0
    node0.next = node_minus_4
    node_minus_4.next = node2  # Create a cycle

    sol = Solution()
    print(f"Has cycle (Example 1): {sol.hasCycle(head1)}")

    # Example 2: No cycle
    head2 = ListNode(1)
    node2_2 = ListNode(2)
    head2.next = node2_2

    print(f"Has cycle (Example 2): {sol.hasCycle(head2)}")

    # Example 3: Single node, no cycle
    head3 = ListNode(1)
    print(f"Has cycle (Example 3): {sol.hasCycle(head3)}")

    # Example 4: Empty list, no cycle
    head4 = None
    print(f"Has cycle (Example 4): {sol.hasCycle(head4)}")
