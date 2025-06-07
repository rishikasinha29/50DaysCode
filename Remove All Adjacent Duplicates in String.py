class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []  # Initialize an empty list to use as a stack

        for char in s:
            # If the stack is not empty and the current character is
            # the same as the top element of the stack, pop the top element.
            if stack and stack[-1] == char:
                stack.pop()
            else:
                # Otherwise, push the current character onto the stack.
                stack.append(char)
        
        # Join the characters in the stack to form the final string.
        return "".join(stack)
