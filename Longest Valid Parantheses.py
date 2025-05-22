class Solution:
    def longestValidParentheses(self, s: str) -> int:
        """
        Given a string containing just the characters '(' and ')', return the
        length of the longest valid (well-formed) parentheses substring.
        """
        max_len = 0
        stack = [-1]  # Initialize stack with -1 to handle the base case for the first valid pair

        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            else:  # char == ')'
                if len(stack) > 1:  # If there's a matching '('
                    stack.pop()
                    max_len = max(max_len, i - stack[-1])
                else:  # No matching '(' or stack only contains -1
                    stack[0] = i # Reset the base for future calculations
        return max_len
