from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Initialize maxSum to the first element (or negative infinity if allowed, but first element is safe here)
        max_so_far = nums[0]
        # Initialize current_max to the first element
        current_max = nums[0]

        # Iterate through the array starting from the second element
        for i in range(1, len(nums)):
            # For each element, decide whether to extend the current subarray
            # or start a new subarray from the current element.
            # We choose the maximum of:
            # 1. The current element itself (starting a new subarray)
            # 2. The current element plus the current_max (extending the current subarray)
            current_max = max(nums[i], current_max + nums[i])

            # Update max_so_far if current_max is greater
            max_so_far = max(max_so_far, current_max)

        return max_so_far
