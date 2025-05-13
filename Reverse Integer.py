class Solution:
    def reverse(self, x: int) -> int:
        is_negative = False
        if x < 0:
            is_negative = True
            x = -x

        reversed_x = 0
        while x > 0:
            digit = x % 10

            # Check for overflow for positive numbers
            if reversed_x > (2**31 - 1) // 10 or (reversed_x == (2**31 - 1) // 10 and digit > 7):
                return 0

            reversed_x = reversed_x * 10 + digit
            x //= 10

        if is_negative:
            reversed_x = -reversed_x
            # Check for underflow for negative numbers
            if reversed_x < -2**31:
                return 0

        return reversed_x
