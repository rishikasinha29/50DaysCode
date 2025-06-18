class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        """
        Finds the single element that appears only once in an array where
        every other element appears twice.

        This solution uses the XOR bitwise operation. The key properties of XOR are:
        - x ^ x = 0 (XORing a number with itself results in 0)
        - x ^ 0 = x (XORing a number with 0 results in the number itself)
        - XOR is commutative and associative (a ^ b ^ c = a ^ (b ^ c) = (a ^ b) ^ c)

        By XORing all elements in the array, all numbers that appear twice will
        cancel each other out (x ^ x = 0), leaving only the single number.

        Args:
            nums: A non-empty list of integers where every element appears twice
                  except for one.

        Returns:
            The single number that appears only once.
        """
        single_number = 0
        for num in nums:
            single_number ^= num
        return single_number
        
