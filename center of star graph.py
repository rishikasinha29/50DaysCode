from collections import Counter

class Solution:
    def findCenter(self, edges: list[list[int]]) -> int:
        # Since it's a star graph, the center node will be part of every edge.
        # We can pick the first two edges and find the common node.
        # Alternatively, we can count the frequency of each node.

        # Method 1: Using the common node in the first two edges (more efficient for star graphs)
        node1_edge1 = edges[0][0]
        node2_edge1 = edges[0][1]

        # Check if node1_edge1 is present in the second edge
        if node1_edge1 == edges[1][0] or node1_edge1 == edges[1][1]:
            return node1_edge1
        else:
            return node2_edge1

        # Method 2: Using Counter (more general, but slightly less efficient for this specific problem)
        # node_counts = Counter()
        # for u, v in edges:
        #     node_counts[u] += 1
        #     node_counts[v] += 1
        #
        # for node, count in node_counts.items():
        #     # In a star graph with n nodes, the center will have a degree of n-1,
        #     # and all other nodes will have a degree of 1.
        #     # The number of edges is n-1.
        #     # So, the center will appear in all n-1 edges.
        #     if count == len(edges):
        #         return node
