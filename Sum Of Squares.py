import math

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        """
        Given a non-negative integer c, decide whether there're two integers a and b
        such that a^2 + b^2 = c.
        """
        left, right = 0, int(math.sqrt(c))
        while left <= right:
            sum_sq = left * left + right * right
            if sum_sq == c:
                return True
            elif sum_sq < c:
                left += 1
            else:
                right -= 1
        return False

if __name__ == '__main__':
    solver = Solution()

    # Example 1
    c1 = 5
    result1 = solver.judgeSquareSum(c1)
    print(f"Input: c = {c1}")
    print(f"Output: {result1}")
    print("-" * 20)

    # Example 2
    c2 = 3
    result2 = solver.judgeSquareSum(c2)
    print(f"Input: c = {c2}")
    print(f"Output: {result2}")
    print("-" * 20)

    # Additional test cases
    c3 = 0
    result3 = solver.judgeSquareSum(c3)
    print(f"Input: c = {c3}")
    print(f"Output: {result3}")
    print("-" * 20)

    c4 = 4
    result4 = solver.judgeSquareSum(c4)
    print(f"Input: c = {c4}")
    print(f"Output: {result4}")
    print("-" * 20)

    c5 = 2
    result5 = solver.judgeSquareSum(c5)
    print(f"Input: c = {c5}")
    print(f"Output: {result5}")
    print("-" * 20)

    c6 = 1
    result6 = solver.judgeSquareSum(c6)
    print(f"Input: c = {c6}")
    print(f"Output: {result6}")
    print("-" * 20)
