class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result = 0
        power = 0
        for char in reversed(columnTitle):
            # Get the 1-based value of the letter
            value = ord(char) - ord('A') + 1
            result += value * (26 ** power)
            power += 1
        return result

# Example Usage:
if __name__ == "__main__":
    solution = Solution()
    print(f"'A' -> {solution.titleToNumber('A')}")
    print(f"'AB' -> {solution.titleToNumber('AB')}")
    print(f"'ZY' -> {solution.titleToNumber('ZY')}")
    print(f"'FXSHRXW' -> {solution.titleToNumber('FXSHRXW')}")
