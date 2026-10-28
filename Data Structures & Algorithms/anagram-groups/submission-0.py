class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Understand
        # input: strs (list of strings)
        # output: list of list of strings (strings grouped by anagram)

        # Plan - Dictionary with sorted word as key, actual words as value

        # create dict
        # loop through strs
        # sort current word and save it to a key 
        # if the key is not in the dictionary, build a empty list to hold words associated to key 
        
        # append each word to the key (builds list of words associated with key)
        # break out of loop and return dictionary values via list 

        seen = {}
        for w in strs:
            key = "".join(sorted(w))

            if key not in seen:
                seen[key] = []
            
            seen[key].append(w)
        
        return list(seen.values())