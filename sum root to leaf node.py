# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        self.total_sum = 0

        def dfs(node, current_number):
            if not node:
                return

            # Append the current node's value to the current_number
            current_number = current_number * 10 + node.val

            # If it's a leaf node, add the current_number to the total_sum
            if not node.left and not node.right:
                self.total_sum += current_number
                return

            # Recursively call for left and right children
            dfs(node.left, current_number)
            dfs(node.right, current_number)

        dfs(root, 0)
        return self.total_sum
