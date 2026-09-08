class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
# Understand: 
# Using arrays to hold elements
# Boolean returns True or false depending on if there's a duplicate 
# Use a HashMap to check if there's duplicate 

#Plan: 
# Loop through Array
# At each element, add current element to HashMap
# If HashMap already has element, then stop loop and return False 
# Else HashMap doesn't have element, keep adding until the end 
# Successful loop, return True 

        duplicateSet = set()

        for index in nums:
            if index not in duplicateSet:
                duplicateSet.add(index)
            else: #otherwise it's already in the hashmap, contains duplicate
                return True
        return False #No duplicates 
        
    

