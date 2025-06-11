# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.count = 0  # To keep track of the number of elements visited
        self.result = -1 # To store the k-th smallest element

        def inorder_traversal(node):
            if not node:
                return

            # Traverse left subtree
            inorder_traversal(node.left)

            # Visit current node
            self.count += 1
            if self.count == k:
                self.result = node.val
                return # We found the k-th smallest, no need to go further

            # Traverse right subtree
            inorder_traversal(node.right)

        inorder_traversal(root)
        return self.result
