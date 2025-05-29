# Definition for a binary tree node.
#class TreeNode:
 #   def __init__(self, val=0, left=None, right=None):
 #       self.val = val
  #      self.left = left
   #     self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.max_diameter = 0  # Global variable to store the maximum diameter found

        def dfs(node):
            if not node:
                return 0  # Depth of an empty tree is 0

            left_depth = dfs(node.left)
            right_depth = dfs(node.right)

            # The diameter passing through the current node would be the sum of
            # the maximum depths of its left and right subtrees.
            self.max_diameter = max(self.max_diameter, left_depth + right_depth)

            # Return the depth of the current subtree rooted at 'node'.
            # It's 1 (for the current node) plus the maximum depth of its children.
            return 1 + max(left_depth, right_depth)

        dfs(root)
        return self.max_diameter
