class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or len(s) <= numRows:
            return s

        rows = [''] * numRows
        current_row = 0
        going_down = False  # True when moving down, False when moving up

        for char in s:
            rows[current_row] += char
            if current_row == 0 or current_row == numRows - 1:
                going_down = not going_down  # Change direction at top/bottom rows

            if going_down:
                current_row += 1
            else:
                current_row -= 1

        return "".join(rows)
