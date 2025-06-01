import collections

# Definition for a binary tree node.
#class TreeNode:
#    def __init__(self, val=0, left=None, right=None):
#        self.val = val
#        self.left = left
#        self.right = right

class Solution:
    def rightSideView(self, root: TreeNode) -> list[int]:
        right_side_view = []
        if not root:
            return right_side_view

        queue = collections.deque([root])

        while queue:
            level_size = len(queue)
            
            # This variable will store the value of the rightmost node at the current level
            rightmost_node_val = None 
            
            for i in range(level_size):
                node = queue.popleft()
                
                # The last node popped from the queue in this level's iteration will be the rightmost
                rightmost_node_val = node.val 
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            # After processing all nodes at the current level, add the rightmost one to the result
            right_side_view.append(rightmost_node_val)
            
        return right_side_view
