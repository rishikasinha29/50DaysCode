from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        """
        Increments a large integer represented as a list of digits by one.

        Args:
            digits: A list of integers representing the digits of a large integer.
                    The digits are ordered from most significant to least significant.
                    The integer does not contain any leading 0's.

        Returns:
            A list of integers representing the digits of the incremented large integer.
        """
        n = len(digits)
        carry = 1
        for i in range(n - 1, -1, -1):
            digits[i] += carry
            carry = digits[i] // 10
            digits[i] %= 10
            if carry == 0:
                break
        if carry == 1:
            digits.insert(0, 1)
        return digits

# Example Usage (This part might be handled by the online judge):
if __name__ == "__main__":
    digits1 = [1, 2, 3]
    result1 = Solution().plusOne(digits1)
    print(f"Input: {digits1}, Output: {result1}")

    digits2 = [4, 3, 2, 1]
    result2 = Solution().plusOne(digits2)
    print(f"Input: {digits2}, Output: {result2}")

    digits3 = [9]
    result3 = Solution().plusOne(digits3)
    print(f"Input: {digits3}, Output: {result3}")
