class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0
        return 1 + (num - 1) % 9

if __name__ == "__main__":
    solution = Solution()

    # Example 1
    num1 = 38
    result1 = solution.addDigits(num1)
    print(f"Input: {num1}, Output: {result1}")

    # Example 2
    num2 = 0
    result2 = solution.addDigits(num2)
    print(f"Input: {num2}, Output: {result2}")

    # Additional Test Cases
    num3 = 9
    result3 = solution.addDigits(num3)
    print(f"Input: {num3}, Output: {result3}")

    num4 = 19
    result4 = solution.addDigits(num4)
    print(f"Input: {num4}, Output: {result4}")

    num5 = 99
    result5 = solution.addDigits(num5)
    print(f"Input: {num5}, Output: {result5}")

    num6 = 12345
    result6 = solution.addDigits(num6)
    print(f"Input: {num6}, Output: {result6}")
