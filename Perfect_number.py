class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        """
        Checks if a given positive integer is a perfect number.

        Args:
            num: The integer to check.

        Returns:
            True if num is a perfect number, False otherwise.
        """
        if num <= 1:
            return False

        divisor_sum = 1
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                divisor_sum += i
                if i * i != num:  # Avoid adding the square root twice for perfect squares
                    divisor_sum += num // i

        return divisor_sum == num

# Example Usage:
if __name__ == "__main__":
    sol = Solution()
    num1 = 28
    print(f"{num1} is a perfect number: {sol.checkPerfectNumber(num1)}")  # Output: True
    num2 = 7
    print(f"{num2} is a perfect number: {sol.checkPerfectNumber(num2)}")   # Output: False
    num3 = 6
    print(f"{num3} is a perfect number: {sol.checkPerfectNumber(num3)}")   # Output: True
    num4 = 1
    print(f"{num4} is a perfect number: {sol.checkPerfectNumber(num4)}")   # Output: False
