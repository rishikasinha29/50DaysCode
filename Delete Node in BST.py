# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return None

        # Case 1: Key is less than root.val, so search in the left subtree
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        # Case 2: Key is greater than root.val, so search in the right subtree
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        # Case 3: Key is equal to root.val, this is the node to be deleted
        else:
            # Subcase 3.1: Node has no left child (or is a leaf node)
            if not root.left:
                return root.right
            # Subcase 3.2: Node has no right child
            elif not root.right:
                return root.left
            # Subcase 3.3: Node has two children
            else:
                # Find the inorder successor (smallest node in the right subtree)
                min_node_in_right_subtree = self._find_min(root.right)
                
                # Replace the current node's value with the inorder successor's value
                root.val = min_node_in_right_subtree.val
                
                # Delete the inorder successor from the right subtree
                root.right = self.deleteNode(root.right, min_node_in_right_subtree.val)
        
        return root

    def _find_min(self, node: TreeNode) -> TreeNode:
        # Helper function to find the minimum node in a subtree
        current = node
        while current.left:
            current = current.left
        return current
        
