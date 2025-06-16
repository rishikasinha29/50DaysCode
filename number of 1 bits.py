class Solution:
    def hammingWeight(self, n: int) -> int:
        """
        Calculates the number of set bits (1s) in the binary representation of an integer.
        This implementation uses Brian Kernighan's algorithm.

        Args:
            n: A positive integer.

        Returns:
            The number of set bits in n.
        """
        count = 0
        while n != 0:
            n &= (n - 1)  # This operation turns off the rightmost set bit
            count += 1
        return count
