# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return

        self.prev = None  # To store the previously visited node in reverse pre-order

        def dfs(node):
            if not node:
                return

            # Traverse right subtree first (reverse pre-order)
            dfs(node.right)
            # Traverse left subtree
            dfs(node.left)

            # Link current node to the previously flattened subtree
            node.right = self.prev
            node.left = None  # Left child should always be null

            # Update prev for the next iteration
            self.prev = node

        dfs(root)
