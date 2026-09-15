class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Neetcode Solution
        
        seen = set()
        l = 0
        maxLength = 0

        for r in range(len(s)): # iterate through string using indices 
            while s[r] in seen: # while a duplicate is found from the right pointer
                seen.remove(s[l]) # remove the character from the left pointer (left pointer & right pointer are duplicates)
                l += 1 # update the pointer
            seen.add(s[r])
            
            window_size = r - l + 1 
            maxLength = max(maxLength, window_size)
        return maxLength