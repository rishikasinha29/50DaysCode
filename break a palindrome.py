class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        n = len(palindrome)

        # Edge case: If the palindrome has only one character,
        # it's impossible to make it non-palindromic by changing one character.
        if n == 1:
            return ""

        # Convert string to a list of characters for mutability
        arr = list(palindrome)

        # Iterate through the first half of the string
        for i in range(n // 2):
            # If we find a character that is not 'a', change it to 'a'
            # This ensures the lexicographically smallest result and breaks the palindrome.
            if arr[i] != 'a':
                arr[i] = 'a'
                return "".join(arr)

        # If we reach here, it means all characters in the first half were 'a's.
        # This implies the entire palindrome consists of 'a's (e.g., "aaaaa").
        # To make it not a palindrome and still get the lexicographically smallest result,
        # we must change the last character to 'b'.
        arr[n - 1] = 'b'
        return "".join(arr)
