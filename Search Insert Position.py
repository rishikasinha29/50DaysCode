class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        """
        Given a sorted array of distinct integers and a target value, return the index if the target is found.
        If not, return the index where it would be if it were inserted in order.

        The algorithm must have O(log n) runtime complexity.
        """
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:  # nums[mid] > target
                right = mid - 1
        
        # If the loop finishes, 'left' will be the correct insertion point.
        # This is because 'left' always points to the first element
        # greater than or equal to the target. If target is larger than
        # all elements, 'left' will be len(nums).
        return left
