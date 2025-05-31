class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Rotates an n x n 2D matrix by 90 degrees clockwise in-place.

        Args:
            matrix: The input square matrix to be rotated.
        """
        n = len(matrix)

        # Step 1: Transpose the matrix
        # Iterate only through the upper triangle (or lower) to avoid double-swapping
        for i in range(n):
            for j in range(i, n): # Start j from i to avoid re-swapping elements
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Step 2: Reverse each row
        for i in range(n):
            matrix[i].reverse() # Python's list.reverse() method reverses in-place
          
