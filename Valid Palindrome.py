class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        Checks if a given string is a palindrome, considering only alphanumeric characters
        and ignoring case.

        Args:
            s: The input string.

        Returns:
            True if the string is a palindrome, False otherwise.
        """
        cleaned_s = ""
        for char in s:
            if 'a' <= char <= 'z' or '0' <= char <= '9':
                cleaned_s += char
            elif 'A' <= char <= 'Z':
                cleaned_s += char.lower()

        # Check if the cleaned string is a palindrome
        return cleaned_s == cleaned_s[::-1]
