# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        """
        Determines if a given binary tree is a valid Binary Search Tree (BST).

        A valid BST is defined as follows:
        - The left subtree of a node contains only nodes with keys less than the node's key.
        - The right subtree of a node contains only nodes with keys greater than the node's key.
        - Both the left and right subtrees must also be binary search trees.

        Args:
            root: The root node of the binary tree.

        Returns:
            True if the tree is a valid BST, False otherwise.
        """
        return self._isValidBST_helper(root, float('-inf'), float('inf'))

    def _isValidBST_helper(self, node: TreeNode, lower_bound: float, upper_bound: float) -> bool:
        """
        Helper function for isValidBST to recursively check BST properties.

        Args:
            node: The current node being checked.
            lower_bound: The minimum allowed value for the current node and its descendants.
            upper_bound: The maximum allowed value for the current node and its descendants.

        Returns:
            True if the subtree rooted at 'node' is a valid BST within the given bounds,
            False otherwise.
        """
        # An empty tree is a valid BST
        if not node:
            return True

        # Check if the current node's value is within the allowed range
        if not (lower_bound < node.val < upper_bound):
            return False

        # Recursively check the left subtree:
        # The left child's value must be less than node.val, so update upper_bound.
        # The lower_bound remains the same.
        if not self._isValidBST_helper(node.left, lower_bound, node.val):
            return False

        # Recursively check the right subtree:
        # The right child's value must be greater than node.val, so update lower_bound.
        # The upper_bound remains the same.
        if not self._isValidBST_helper(node.right, node.val, upper_bound):
            return False

        # If all checks pass, the current subtree is a valid BST
        return True
