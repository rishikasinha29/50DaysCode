class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        Helper function to check if a string is a palindrome.
        A string is palindromic if it reads the same forward and backward.
        """
        return s == s[::-1]

    def firstPalindrome(self, words: list[str]) -> str:
        """
        Given an array of strings, return the first palindromic string in the array.
        If there is no such string, return an empty string "".
        """
        for word in words:
            if self.isPalindrome(word):
                return word
        return ""
