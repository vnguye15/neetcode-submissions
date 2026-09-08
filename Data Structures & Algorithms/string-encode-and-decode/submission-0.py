class Solution:


    #neetcode solution
    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res
    
    def decode(self, s: str) -> List[str]: 
        res, i = [], 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j]) # Grabs char from i to j -> [inclusive:non-inclusive] 
            res.append(s[j + 1: j + 1 + length])
            i = j + 1 + length
        return res    











    # Understand
    # encode takes in a list of strings and converts into one single string 
    # decode: converts the single string back into a list of strings 
    # Potential String methods: Splicing, Join, Split (delimiter)

    # Constraints
    # Convert strings to lowercase to avoid any confusion 

    # Plan

    # (encode) 
    # First convert each string into a lower case 
    # Join strings together into one single string 

    # (decode)
    # From single string, separate each 
