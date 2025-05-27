import collections

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        # Use a deque for efficient appends and pops from both ends (BFS queue)
        queue = collections.deque([(root, 1)])  # (node, current_depth)

        while queue:
            node, depth = queue.popleft()

            # If it's a leaf node, we've found the shortest path
            if not node.left and not node.right:
                return depth

            # Otherwise, add children to the queue with incremented depth
            if node.left:
                queue.append((node.left, depth + 1))
            if node.right:
                queue.append((node.right, depth + 1))

        # This part should ideally not be reached if the tree has at least one node
        return 0

# Helper function to build a tree from a list (for testing purposes)
def build_tree(nodes):
    if not nodes:
        return None

    root = TreeNode(nodes[0])
    queue = collections.deque([root])
    i = 1
    while queue and i < len(nodes):
        current_node = queue.popleft()
        if nodes[i] is not None:
            current_node.left = TreeNode(nodes[i])
            queue.append(current_node.left)
        i += 1
        if i < len(nodes) and nodes[i] is not None:
            current_node.right = TreeNode(nodes[i])
            queue.append(current_node.right)
        i += 1
    return root

# Example Usage:
if __name__ == "__main__":
    solver = Solution()

    # Example 1:
    # Input: root = [3,9,20,null,null,15,7]
    # Output: 2
    root1 = build_tree([3, 9, 20, None, None, 15, 7])
    print(f"Example 1 Output: {solver.minDepth(root1)}") # Expected: 2

    # Example 2:
    # Input: root = [2,null,3,null,4,null,5,null,6]
    # Output: 5
    root2 = build_tree([2, None, 3, None, 4, None, 5, None, 6])
    print(f"Example 2 Output: {solver.minDepth(root2)}") # Expected: 5

    # Example with a single node
    root3 = build_tree([1])
    print(f"Single Node Output: {solver.minDepth(root3)}") # Expected: 1

    # Example with an empty tree
    root4 = build_tree([])
    print(f"Empty Tree Output: {solver.minDepth(root4)}") # Expected: 0
