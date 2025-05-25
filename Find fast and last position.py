class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        first_occurrence = self._find_first(nums, target)
        if first_occurrence == -1:
            return [-1, -1]
        
        last_occurrence = self._find_last(nums, target)
        return [first_occurrence, last_occurrence]

    def _find_first(self, nums: list[int], target: int) -> int:
        """
        Finds the first occurrence of the target in the sorted array.
        Returns -1 if not found.
        """
        left, right = 0, len(nums) - 1
        first_idx = -1

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                first_idx = mid
                right = mid - 1  # Try to find an earlier occurrence in the left half
            elif nums[mid] < target:
                left = mid + 1
            else:  # nums[mid] > target
                right = mid - 1
        return first_idx

    def _find_last(self, nums: list[int], target: int) -> int:
        """
        Finds the last occurrence of the target in the sorted array.
        Returns -1 if not found (though this function is only called if first_occurrence is found).
        """
        left, right = 0, len(nums) - 1
        last_idx = -1

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                last_idx = mid
                left = mid + 1  # Try to find a later occurrence in the right half
            elif nums[mid] < target:
                left = mid + 1
            else:  # nums[mid] > target
                right = mid - 1
        return last_idx
