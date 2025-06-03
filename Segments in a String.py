class Solution:
    def countSegments(self, s: str) -> int:
        """
        Counts the number of segments in a string.
        A segment is defined as a contiguous sequence of non-space characters.
        """
        if not s:
            return 0

        count = 0
        in_segment = False

        for char in s:
            if char != ' ':
                # If we encounter a non-space character and were not already in a segment,
                # it means a new segment has started.
                if not in_segment:
                    count += 1
                    in_segment = True
            else:
                # If we encounter a space, we are no longer in a segment.
                in_segment = False
        return count

# Example Usage (from the image)
if __name__ == "__main__":
    solution = Solution()

    # Example 1
    s1 = "Hello, my name is John"
    result1 = solution.countSegments(s1)
    print(f"Input: \"{s1}\"")
    print(f"Output: {result1}")  # Expected: 5

    # Example 2
    s2 = "Hello"
    result2 = solution.countSegments(s2)
    print(f"Input: \"{s2}\"")
    print(f"Output: {result2}")  # Expected: 1

    # Additional Test Cases:
    s3 = ""
    result3 = solution.countSegments(s3)
    print(f"Input: \"{s3}\"")
    print(f"Output: {result3}")  # Expected: 0

    s4 = " "
    result4 = solution.countSegments(s4)
    print(f"Input: \"{s4}\"")
    print(f"Output: {result4}")  # Expected: 0

    s5 = "   a   b c d  "
    result5 = solution.countSegments(s5)
    print(f"Input: \"{s5}\"")
    print(f"Output: {result5}")  # Expected: 4

    s6 = ", , , ,        a, eaefa"
    result6 = solution.countSegments(s6)
    print(f"Input: \"{s6}\"")
    print(f"Output: {result6}")  # Expected: 6
