class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        """
        Finds the majority element in an array using Boyer-Moore Voting Algorithm.
        The majority element is the element that appears more than floor(n / 2) times.
        It's guaranteed that the majority element always exists in the array.

        Args:
            nums: A list of integers.

        Returns:
            The majority element.
        """
        count = 0
        candidate = 0

   
        for num in nums:
            if count == 0:
                # If count is 0, it means the previous candidate's votes have been
                # "canceled out" by other elements. We pick the current element as a new candidate.
                candidate = num
            
            # If the current number is the same as the candidate, increment the count (vote for candidate).
            if num == candidate:
                count += 1
            # If the current number is different from the candidate, decrement the count (vote against candidate).
            else:
                count -= 1
        
        # After the loop, 'candidate' will hold the majority element.
        # The problem statement guarantees that the majority element always exists,
        # so a second pass to verify the candidate's count is not strictly necessary.
        # If it wasn't guaranteed, we would need to count occurrences of 'candidate'
        # in a second loop and check if it indeed appears > n/2 times.

        return candidate
