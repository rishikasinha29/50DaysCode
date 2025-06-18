class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0

        # Create a boolean array "is_prime[0..n-1]" and initialize
        # all entries it as true. A value in is_prime[i] will
        # finally be false if i is Not a prime, else true.
        is_prime = [True] * n
        is_prime[0] = is_prime[1] = False # 0 and 1 are not prime numbers

        # Start checking from p = 2 up to sqrt(n)
        # We only need to iterate up to sqrt(n) because if n has a factor
        # larger than sqrt(n), it must also have a factor smaller than sqrt(n).
        for p in range(2, int(n**0.5) + 1):
            # If is_prime[p] is still true, then it is a prime
            if is_prime[p]:
                # Update all multiples of p as not prime
                # We start from p*p because smaller multiples (like 2*p, 3*p, etc.)
                # would have already been marked by smaller primes (like 2, 3, etc.)
                for multiple in range(p * p, n, p):
                    is_prime[multiple] = False

        # Count all prime numbers
        count = 0
        for i in range(2, n):
            if is_prime[i]:
                count += 1
        return count
