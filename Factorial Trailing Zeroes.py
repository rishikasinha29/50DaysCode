class Solution:
    def trailingZeroes(self, n: int) -> int:
        """
        Calculates the number of trailing zeros in the factorial of a non-negative integer.

        The number of trailing zeros in n! is determined by the number of times 10 is a factor in its prime factorization.
        Since 10 = 2 * 5, we need to count the number of pairs of 2 and 5 in the prime factorization of n!.
        There will always be more factors of 2 than 5, so we only need to count the number of factors of 5.

        Args:
            n: A non-negative integer.

        Returns:
            The number of trailing zeros in n!.
        """
        count = 0
        i = 5
        while n // i >= 1:
            count += n // i
            i *= 5
        return count
