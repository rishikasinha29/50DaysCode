# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # If the tree is empty, create a new node and return it as the root.
        if not root:
            return TreeNode(val)

        # Traverse the tree to find the correct position for insertion.
        # We start from the root and go down.
        current = root
        while current:
            if val < current.val:
                # If val is less than the current node's value,
                # go to the left subtree.
                if current.left is None:
                    # If left child is None, we found the spot for insertion.
                    current.left = TreeNode(val)
                    break # Insertion complete
                else:
                    current = current.left
            else: # val > current.val (since val is guaranteed not to exist, no need for equality check)
                # If val is greater than the current node's value,
                # go to the right subtree.
                if current.right is None:
                    # If right child is None, we found the spot for insertion.
                    current.right = TreeNode(val)
                    break # Insertion complete
                else:
                    current = current.right
        
        return root
