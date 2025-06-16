import math

class Solution:
    def isGoodArray(self, nums: list[int]) -> bool:
        """
        Checks if a given array is a 'good array'.

        An array is good if a sum of 1 can be obtained by selecting a subset of nums,
        multiplying each element by an integer, and adding them.
        This is possible if and only if the greatest common divisor (GCD) of all
        elements in the array is 1 (Bézout's identity).
        """
        if not nums:
            return False  # An empty array cannot form a sum of 1

        # Initialize the current_gcd with the first element of the array
        current_gcd = nums[0]

        # Iterate through the rest of the elements and compute the GCD cumulatively
        for i in range(1, len(nums)):
            current_gcd = math.gcd(current_gcd, nums[i])

            # If the GCD becomes 1 at any point, we can stop early
            # because the GCD of 1 and any other number will always be 1.
            if current_gcd == 1:
                return True

        # After checking all elements, if the GCD is 1, return True, otherwise False
        return current_gcd == 1
