import math

class Solution:
    def bulbSwitch(self, n: int) -> int:
        return int(math.sqrt(n))

# Example Usage:
solution = Solution()
print(solution.bulbSwitch(3))   # Output: 1
print(solution.bulbSwitch(0))   # Output: 0
print(solution.bulbSwitch(1))   # Output: 1
print(solution.bulbSwitch(4))   # Output: 2
print(solution.bulbSwitch(9))   # Output: 3
