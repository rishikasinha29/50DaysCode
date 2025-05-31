# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections

class Solution:
    def levelOrder(self, root: TreeNode) -> list[list[int]]:
        """
        Performs a level order traversal (BFS) of a binary tree.

        Args:
            root: The root node of the binary tree.

        Returns:
            A list of lists, where each inner list contains the values
            of nodes at a specific level.
        """
        if not root:
            return []

        result = []
        queue = collections.deque([root]) # Initialize a deque with the root node

        while queue:
            level_size = len(queue)  # Number of nodes at the current level
            current_level_nodes = [] # To store values of nodes at the current level

            for _ in range(level_size):
                node = queue.popleft() # Dequeue a node
                current_level_nodes.append(node.val) # Add its value to the current level list

                # Enqueue children if they exist
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(current_level_nodes) # Add the current level's values to the result

        return result
        
