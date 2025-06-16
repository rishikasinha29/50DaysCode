class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        """
        Calculates the number of substrings containing at least one occurrence
        of all three characters 'a', 'b', and 'c'.

        Args:
            s: The input string consisting only of 'a', 'b', or 'c'.

        Returns:
            The total number of such valid substrings.
        """
        count = 0
        left = 0
        # Use a dictionary to store counts of 'a', 'b', 'c' in the current window
        char_counts = {'a': 0, 'b': 0, 'c': 0}
        n = len(s)

        for right in range(n):
            # Expand the window to the right
            char_counts[s[right]] += 1

            # While the current window is valid (contains at least one of 'a', 'b', 'c')
            while char_counts['a'] > 0 and char_counts['b'] > 0 and char_counts['c'] > 0:
                # If s[left:right+1] is valid, then all substrings starting at 'left'
                # and ending at 'right' or any point after 'right' are also valid.
                # The number of such substrings is (n - 1 - right + 1) = n - right.
                count += (n - right)

                # Shrink the window from the left
                char_counts[s[left]] -= 1
                left += 1
        
        return count
