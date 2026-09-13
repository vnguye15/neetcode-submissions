class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # Understand
        # input: s (type string), t (type string) 
        # output: True/False (boolean)
        
        # Questions
        # Can strings s and t be different size? 
        # If they are different size, is False still returned? 
        

        # Plan
        # (Approach): dictionary that will compare the string of s to the string of t

        # Create a dictionary (key:val) that stores char and returns occurence 
        # loop through string s 
        # if current char is not in dictionary --> add it to dictionary and give it a value of 1
        # else update value with 1 

        # loop through string t 
        # if current char is in dictionary --> subtract 1 from the value and continue 
        # else char is not in dict --> return False 

        # if dictionary values are not 0, then return false 

        # Case: length of strings different
        if len(s) != len(t):
            return False

        seen = {}
        for c in s:
            if c not in seen:
                seen[c] = 1 
            else:
                seen[c] += 1 
        
        for char in t:
            if char in seen:
                seen[char] -= 1 
            else:
                return False

        # Case to check dictionary values
        for val in seen: 
            if seen[val] != 0: # 
                return False
        return True


                