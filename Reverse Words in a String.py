class Solution:
    def reverseWords(self, s: str) -> str:
        """
        Reverses the order of words in a given input string.

        A word is defined as a sequence of non-space characters.
        The words in s will be separated by at least one space.

        The returned string should only have a single space separating the words.
        It should not include any extra spaces (leading or trailing).

        Args:
            s: The input string.

        Returns:
            The string with the order of words reversed.
        """
        # Step 1: Split the string by spaces to get a list of words.
        # The split() method without arguments handles multiple spaces and
        # leading/trailing spaces by returning empty strings, which we'll filter out.
        words = s.split(' ')

        # Step 2: Filter out any empty strings that result from multiple spaces
        # or leading/trailing spaces.
        filtered_words = [word for word in words if word]

        # Step 3: Reverse the order of the filtered words.
        filtered_words.reverse() # In-place reversal

        # Step 4: Join the reversed words with a single space.
        return ' '.join(filtered_words)
