class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        n = len(s)
        s_list = list(s)  # Convert string to list of characters for mutability

        left = 0
        right = n - 1

        while left < right:
            if s_list[left] != s_list[right]:
                # To make it lexicographically smallest, choose the smaller character
                # and assign it to both positions.
                if s_list[left] < s_list[right]:
                    s_list[right] = s_list[left]
                else:
                    s_list[left] = s_list[right]
            
            left += 1
            right -= 1
            
        return "".join(s_list) # Convert list of characters back to string
