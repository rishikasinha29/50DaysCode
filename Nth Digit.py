class Solution:
    def findNthDigit(self, n: int) -> int:
        digit_length = 1
        count = 9
        while n > digit_length * count:
            n -= digit_length * count
            digit_length += 1
            count *= 10

        # Now we know the nth digit is in a number with 'digit_length' digits
        # and it's the 'n'th digit among all such numbers.

        # Determine which number contains the nth digit
        number_index = (n - 1) // digit_length
        start_number = 10**(digit_length - 1)
        target_number = start_number + number_index

        # Determine which digit within the target number is the nth digit
        digit_index = (n - 1) % digit_length
        return int(str(target_number)[digit_index])
