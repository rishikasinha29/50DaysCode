class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""

        # Take the first string as the initial prefix
        prefix = strs[0]

        # Iterate through the rest of the strings
        for i in range(1, len(strs)):
            current_string = strs[i]
            
            # Reduce the prefix until it's a prefix of the current string
            while current_string.find(prefix) != 0:
                prefix = prefix[:-1] # Remove the last character
                if not prefix: # If prefix becomes empty, no common prefix exists
                    return ""
        
        return prefix
