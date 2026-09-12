class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        # Plan
        # first lowercase string, then clean it 
        # create a new string that will only have alphanumeric characters
        # check if each char is between a-z oro 0-9
        # if it is then add it to our new string 

        # (cleaned string)
        # create left and right pointers: left at first index and right at last index 
        # while left pointer has not crossed over right pointer:
        # move pointers closer towards middle 
        # if char of left pointer is different than char of right pointer, return false

        # otherwise return True

        string = s.lower()

        # Cleaning string 
        clean = ""
        for char in string:
            if ('a' <= char <= 'z') or ('0' <= char <= '9'):
                clean += char # append each character to the string 
        
        left = 0
        right = len(clean) - 1 
        while left < right:
            if clean[left] != clean[right]:
                return False

            left += 1 
            right -= 1

        return True