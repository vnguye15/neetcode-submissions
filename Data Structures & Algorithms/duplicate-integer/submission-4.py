class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        #Understand
        # input: list with elements
        # output: boolean true or false 
        # true if there is a duplicate, false if there isn't 
        # duplicate --> repeating number in list 

        # plan 
        # Go through the list 
        # Add each value to data structure 
        # If element saved already exists in that data structure (set --> unique value only
        # then return True 
        # Otherwise return False  
        
        
        
        duplicates = set()
        for index in range(len(nums)): # using range(len((list))) lets us maintain safety
            if nums[index] not in duplicates: # if our value is NOT in the set
                duplicates.add(nums[index]) #add it to our set   
            else: # otherwise it is in our set 
                return True  
        return False 
                
            