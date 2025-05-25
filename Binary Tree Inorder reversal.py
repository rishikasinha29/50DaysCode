# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: TreeNode) -> list[int]:
        result = []

        def inorder_recursive(node):
            if not node:
                return
            inorder_recursive(node.left)  # Traverse left subtree
            result.append(node.val)      # Visit root
            inorder_recursive(node.right) # Traverse right subtree

        inorder_recursive(root)
        return result
