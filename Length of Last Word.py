class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # Step 1: Trim leading/trailing spaces
        s = s.strip()

        # Step 2: Split the string by spaces
        # split() without arguments handles multiple spaces between words
        # and automatically removes empty strings resulting from those spaces.
        words = s.split(' ')

        # Step 3: Get the last word and return its length
        # Since the problem guarantees at least one word, words list will not be empty.
        return len(words[-1])
