class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        # Pre-define a set of prime numbers up to the maximum possible set bits
        # For numbers up to 10^9, max set bits is around 30 (e.g., 2^30 - 1 has 30 set bits)
        # Primes up to 30: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29
        prime_numbers = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29}

        count = 0
        for num in range(left, right + 1):
            # Count set bits (number of '1's in binary representation)
            # bin(num) returns a string like '0b10110'
            set_bits = bin(num).count('1')

            # Check if the number of set bits is prime
            if set_bits in prime_numbers:
                count += 1
        return count
