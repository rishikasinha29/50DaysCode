class Solution:
    def isHappy(self, n: int) -> bool:
        """
        Determines if a number is a happy number.

        A happy number is defined by the following process:
        - Starting with any positive integer, replace the number by the sum of the squares of its digits.
        - Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
        - Those numbers for which this process ends in 1 are happy.

        Args:
            n: The integer to check.

        Returns:
            True if n is a happy number, False otherwise.
        """
        seen = set()  # Use a set to keep track of seen numbers to detect cycles

        while n != 1 and n not in seen:
            seen.add(n)  # Add the current number to the set
            n = self.sum_of_squares(n)  # Calculate the sum of the squares of the digits

        return n == 1  # If n is 1, it's a happy number

    def sum_of_squares(self, num: int) -> int:
        """
        Calculates the sum of the squares of the digits of a number.

        Args:
            num: The integer.

        Returns:
            The sum of the squares of the digits.
        """
        sum_sq = 0
        while num > 0:
            digit = num % 10  # Get the last digit
            sum_sq += digit * digit  # Square the digit and add it to the sum
            num //= 10  # Remove the last digit
        return sum_sq
