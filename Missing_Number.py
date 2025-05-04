from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        expected_sum = n * (n + 1) // 2
        actual_sum = sum(nums)
        return expected_sum - actual_sum

# Example Usage:
if __name__ == "__main__":
    solution = Solution()

    # Example 1
    nums1 = [3, 0, 1]
    missing1 = solution.missingNumber(nums1)
    print(f"Input: {nums1}, Missing Number: {missing1}")

    # Example 2
    nums2 = [0, 1]
    missing2 = solution.missingNumber(nums2)
    print(f"Input: {nums2}, Missing Number: {missing2}")

    # Example 3
    nums3 = [9, 6, 4, 2, 3, 5, 7, 0, 1]
    missing3 = solution.missingNumber(nums3)
    print(f"Input: {nums3}, Missing Number: {missing3}")

    # Additional Test Cases
    nums4 = [0]
    missing4 = solution.missingNumber(nums4)
    print(f"Input: {nums4}, Missing Number: {missing4}")

    nums5 = [1]
    missing5 = solution.missingNumber(nums5)
    print(f"Input: {nums5}, Missing Number: {missing5}")

    nums6 = [0, 2, 3]
    missing6 = solution.missingNumber(nums6)
    print(f"Input: {nums6}, Missing Number: {missing6}")
