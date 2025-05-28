# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        return self._helper(root, False)

    def _helper(self, node: Optional[TreeNode], is_left: bool) -> int:
        if node is None:
            return 0

        # Check if the current node is a left leaf
        if is_left and node.left is None and node.right is None:
            return node.val

        # Recursively sum left leaves from left and right subtrees
        left_sum = self._helper(node.left, True)  # Mark left child as 'is_left'
        right_sum = self._helper(node.right, False) # Right child is not 'is_left'

        return left_sum + right_sum
