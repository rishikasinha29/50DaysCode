class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        # XORing x and y will result in a number where
        # set bits (1s) indicate positions where x and y differ.
        xor_result = x ^ y

        # Count the number of set bits in xor_result.
        # This can be done by repeatedly right-shifting and checking the last bit,
        # or by using the Brian Kernighan's algorithm.

        count = 0
        while xor_result > 0:
            xor_result &= (xor_result - 1)  # Brian Kernighan's algorithm
            count += 1
        return count
