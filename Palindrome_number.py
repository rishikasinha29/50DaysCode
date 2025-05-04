class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Negative numbers are not palindromes
        if x < 0:
            return False

        # Single-digit numbers are palindromes
        if 0 <= x < 10:
            return True

        reversed_x = 0
        original_x = x

        while x > 0:
            digit = x % 10
            reversed_x = reversed_x * 10 + digit
            x //= 10

        return original_x == reversed_x

# Example Usage:
if __name__ == '__main__':
    sol = Solution()
    print(f"Is 121 a palindrome? {sol.isPalindrome(121)}")
    print(f"Is -121 a palindrome? {sol.isPalindrome(-121)}")
    print(f"Is 10 a palindrome? {sol.isPalindrome(10)}")
    print(f"Is 0 a palindrome? {sol.isPalindrome(0)}")
    print(f"Is 12321 a palindrome? {sol.isPalindrome(12321)}")
