class Solution:
    def isValid(self, s: str) -> bool:
        """
        Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
        determine if the input string is valid.

        An input string is valid if:
        1. Open brackets must be closed by the same type of brackets.
        2. Open brackets must be closed in the correct order.
        3. Every close bracket has a corresponding open bracket of the same type.

        Example 1:
        Input: s = "()"
        Output: true

        Example 2:
        Input: s = "()[]{}"
        Output: true

        Example 3:
        Input: s = "(]"
        Output: false

        Example 4:
        Input: s = "([)]"
        Output: false

        Example 5:
        Input: s = "{[]}"
        Output: true

        Constraints:
        1 <= s.length <= 10^4
        s consists of parentheses only '()[]{}'.
        """
        stack = []
        mapping = {")": "(", "}": "{", "]": "["}

        for char in s:
            if char in mapping:
                top_element = stack.pop() if stack else '#'
                if mapping[char] != top_element:
                    return False
            else:
                stack.append(char)

        return not stack

# Example Usage:
solution = Solution()
s1 = "()"
print(f'isValid("{s1}"): {solution.isValid(s1)}')

s2 = "()[]{}"
print(f'isValid("{s2}"): {solution.isValid(s2)}')

s3 = "(]"
print(f'isValid("{s3}"): {solution.isValid(s3)}')

s4 = "([)]"
print(f'isValid("{s4}"): {solution.isValid(s4)}')

s5 = "{[]}"
print(f'isValid("{s5}"): {solution.isValid(s5)}')
