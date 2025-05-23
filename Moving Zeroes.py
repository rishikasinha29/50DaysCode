class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        write_pointer = 0

        for read_pointer in range(len(nums)):
            if nums[read_pointer] != 0:
                if read_pointer != write_pointer:
                    nums[write_pointer], nums[read_pointer] = nums[read_pointer], nums[write_pointer]
                write_pointer += 1
