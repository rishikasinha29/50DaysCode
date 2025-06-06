# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        """
        Searches for a node with the given value in a Binary Search Tree (BST).

        Args:
            root: The root of the Binary Search Tree.
            val: The integer value to search for.

        Returns:
            The subtree rooted at the node with the given value if found,
            otherwise None.
        """
        if not root:
            return None

        if root.val == val:
            return root
        elif val < root.val:
            # If the target value is smaller, search in the left subtree
            return self.searchBST(root.left, val)
        else:
            # If the target value is larger, search in the right subtree
            return self.searchBST(root.right, val)
