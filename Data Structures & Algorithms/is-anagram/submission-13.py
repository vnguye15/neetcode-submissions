class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Understand
        # inputs: s (string), t (string)
        # output: True/False (bool)

        # return True if both strings contain same characters 
        # return False if both strings contain different characters 

        # Conditions:
        # if string s and string t lengths are different --> return False (different characters)

        # Plan - Dictionary 
        # Using a dictionary that stores characters:character frequency (key:val)

        # check if length s different than length t:
        #   return false  
        
        # (Building data structure)
        # Create dictionary
        # loop through s string
        # if char not in dictionary, add it 
        # otherwise char is in dictionary, update occurence

        # (Comparing t string to data structure)
        # loop through t string
        # if current char exists in dictionary: 
        #  subtract 1 from current char's frequency count 
        # else current char does not exist in dictionary, return False

        # (checking dictionary for leftover values)
        # loop through dictionary vals
        # if dictionary length equals 0:
        # return True

        seen = {}

        if len(s) != len(t):
            return False

        for c in s:
            if c not in seen:
                seen[c] = 1
            else:
                seen[c] += 1
        
        for n in t:
            if n in seen:
                seen[n] -= 1 
            # else:
            #     return False 

        # debugging:
        # seen = {r:2, a:2, c:2, e:1}
        
        # return len(seen) == 0

        for val in seen.values():
            if val != 0:
                return False
        return True
            


