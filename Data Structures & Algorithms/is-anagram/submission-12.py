class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # Understand
        # input: s and t (type strings)
        # output: True/False (boolean)
        # Anagrams are True if they both have same characters 

        # Approach - frequency count
        
        # Plan

        # Building Dictionary
        # create a dictionary
        # iterate through string s 
        # if char not in dictionary
        #   add each character of s 
        # else char is in dictionary:
        #   update char value
        

        # Comparing t string to dictionary
        # iterate through t 
        # if current char exists in dict:
        #      subtract 1 from value of dict
        # otherwise return false immediately 

        # Checking Dictionary is Empty for True/False
        # iterate through dictionary values
        # if current value is not 0
        #  return False 

        # return True 

        freq = {}
        for c in s: 
            if c not in freq:
                freq[c] = 1
            else:
                freq[c] += 1 
        
        for i in t: 
            if i in freq:
                freq[i] -= 1 
            else:
                return False
        
        for val in freq.values():
            if val != 0:
                return False
        return True
