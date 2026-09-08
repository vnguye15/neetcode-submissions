class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Input: integer array 
        # Output: Boolean that returns True / False 

        # Plan 
        # creating hash map 
        # iterate through array 
        # if number does not exist, add number as keys to hashmap
        # if number exist, return true

        map = {}
        for num in nums: 
            if num not in map: 
                map[num] = 1 #number not seen, add 1 to the value @ key
            else: #otherwise number in the array is in the hashmap, return True
                return True
                
        # return False 
        return False
