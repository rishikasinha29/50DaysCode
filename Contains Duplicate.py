from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        Given an integer array nums, return true if any value appears at least twice in the array,
        and return false if every element is distinct.
        """
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False

# Example Usage:
solution = Solution()

# Example 1
nums1 = [1, 2, 3, 1]
result1 = solution.containsDuplicate(nums1)
print(f"Input: {nums1}, Output: {result1}")  # Output: True

# Example 2
nums2 = [1, 2, 3, 4]
result2 = solution.containsDuplicate(nums2)
print(f"Input: {nums2}, Output: {result2}")  # Output: False

# Example 3
nums3 = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
result3 = solution.containsDuplicate(nums3)
print(f"Input: {nums3}, Output: {result3}")  # Output: True
