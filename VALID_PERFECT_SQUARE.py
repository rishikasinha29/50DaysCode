class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num < 0:
            return False
        if num == 0 or num == 1:
            return True

        low = 1
        high = num

        while low <= high:
            mid = low + (high - low) // 2
            square = mid * mid

            if square == num:
                return True
            elif square < num:
                low = mid + 1
            else:
                high = mid - 1

        return False

# Example Usage:
if __name__ == "__main__":
    solution = Solution()
    print(f"Is 16 a perfect square? {solution.isPerfectSquare(16)}")
    print(f"Is 14 a perfect square? {solution.isPerfectSquare(14)}")
    print(f"Is 0 a perfect square? {solution.isPerfectSquare(0)}")
    print(f"Is 1 a perfect square? {solution.isPerfectSquare(1)}")
    print(f"Is 9 a perfect square? {solution.isPerfectSquare(9)}")
    print(f"Is 10 a perfect square? {solution.isPerfectSquare(10)}")
    print(f"Is 25 a perfect square? {solution.isPerfectSquare(25)}")
