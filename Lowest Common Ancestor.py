# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Base case: if root is None, or root is p or q, then root is the LCA
        # (since p and q can be descendants of themselves)
        if root is None or root == p or root == q:
            return root

        # Recursively search in the left subtree
        left_lca = self.lowestCommonAncestor(root.left, p, q)
        # Recursively search in the right subtree
        right_lca = self.lowestCommonAncestor(root.right, p, q)

        # If both left_lca and right_lca are not None,
        # it means p and q are found in different subtrees (one in left, one in right).
        # In this case, the current root is the LCA.
        if left_lca and right_lca:
            return root
        # If only left_lca is not None, it means both p and q are in the left subtree,
        # or one of them is left_lca itself and the other is in its subtree.
        # So, left_lca is the LCA.
        elif left_lca:
            return left_lca
        # If only right_lca is not None, it means both p and q are in the right subtree,
        # or one of them is right_lca itself and the other is in its subtree.
        # So, right_lca is the LCA.
        else:
            return right_lca
