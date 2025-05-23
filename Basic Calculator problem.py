class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        operand = 0
        result = 0
        sign = 1  # 1 for positive, -1 for negative

        for char in s:
            if char.isdigit():
                operand = operand * 10 + int(char)
            elif char == '+':
                result += sign * operand
                sign = 1
                operand = 0
            elif char == '-':
                result += sign * operand
                sign = -1
                operand = 0
            elif char == '(':
                # Push the current result and sign onto the stack
                stack.append(result)
                stack.append(sign)
                # Reset result and sign for the new sub-expression
                result = 0
                sign = 1
            elif char == ')':
                result += sign * operand  # Add the last operand within the parentheses
                operand = 0 # Reset operand after processing closing parenthesis
                # Pop the sign and previous result from the stack
                prev_sign = stack.pop()
                prev_result = stack.pop()
                result = prev_result + prev_sign * result
            # Ignore spaces
            elif char == ' ':
                continue
        
        # Add the last operand if any
        if operand != 0:
            result += sign * operand

        return result
