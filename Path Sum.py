# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # Base case: if the tree is empty, there are no paths, so return False
        if not root:
            return False

        # If it's a leaf node, check if the remaining targetSum equals the current node's value
        if not root.left and not root.right:
            return targetSum == root.val

        # Recursively call for left and right children
        # Subtract the current node's value from the targetSum for the next level
        left_has_sum = self.hasPathSum(root.left, targetSum - root.val)
        right_has_sum = self.hasPathSum(root.right, targetSum - root.val)

        # Return True if either the left or right subtree has a path with the remaining sum
        return left_has_sum or right_has_sum
