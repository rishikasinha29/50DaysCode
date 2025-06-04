class Solution:
    def reverseVowels(self, s: str) -> str:
        s_list = list(s)  # Convert string to a list of characters for mutability
        vowels = "aeiouAEIOU"
        
        left = 0
        right = len(s_list) - 1
        
        while left < right:
            # Move left pointer until a vowel is found
            while left < right and s_list[left] not in vowels:
                left += 1
            
            # Move right pointer until a vowel is found
            while left < right and s_list[right] not in vowels:
                right -= 1
            
            # If both pointers found vowels, swap them
            if left < right:
                s_list[left], s_list[right] = s_list[right], s_list[left]
                left += 1
                right -= 1
        
        return "".join(s_list)
