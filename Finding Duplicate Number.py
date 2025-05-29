class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        # Phase 1: Find the intersection point of the two pointers.
        slow = nums[0]
        fast = nums[0]

        while True:
            slow = nums[slow]          # Move slow by one step
            fast = nums[nums[fast]]    # Move fast by two steps
            if slow == fast:
                break

        # Phase 2: Find the "entrance" to the cycle.
        # This entrance is the duplicate number.
        pointer1 = nums[0]
        pointer2 = slow  # Or fast, they are at the same intersection point

        while pointer1 != pointer2:
            pointer1 = nums[pointer1]
            pointer2 = nums[pointer2]
        
        return pointer1 # Or pointer2, as they meet at the duplicate
