class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Rotates the array to the right by k steps using slicing.
        This approach is concise but typically uses O(N) extra space
        for the new array created by slicing.
        """
        n = len(nums)
        k = k % n  # Handle cases where k is greater than n

        # Slice the array into two parts and concatenate them
        # The last k elements come first, followed by the first n-k elements
        nums[:] = nums[n - k:] + nums[:n - k]

        # Do not return anything, modify nums in-place instead as per problem
