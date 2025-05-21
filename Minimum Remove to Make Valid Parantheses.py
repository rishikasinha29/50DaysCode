class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        chars = list(s)

        open_parentheses_count = 0
        for i in range(len(chars)):
            if chars[i] == '(':
                open_parentheses_count += 1
            elif chars[i] == ')':
                if open_parentheses_count > 0:
                    open_parentheses_count -= 1
                else:
                    chars[i] = ''

        for i in range(len(chars) - 1, -1, -1):
            if open_parentheses_count > 0 and chars[i] == '(':
                chars[i] = ''
                open_parentheses_count -= 1

        return "".join(chars)
