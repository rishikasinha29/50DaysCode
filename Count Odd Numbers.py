class Solution:
    def countOdds(self, low: int, high: int) -> int:
        if low % 2 == 0:
            low += 1
        if high % 2 == 0:
            high -= 1

        if low > high:
            return 0
        else:
            return (high - low) // 2 + 1

# Example usage (optional, for your own testing):
if __name__ == "__main__":
    solver = Solution()
    result1 = solver.countOdds(3, 7)
    print(f"Count between 3 and 7: {result1}")  # Output: 3
    result2 = solver.countOdds(8, 10)
    print(f"Count between 8 and 10: {result2}") # Output: 1
