class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # U

        # output: nums (integer array)
        # input: true/false (boolean)

        # return true if array has duplicates
        # return false if array has no duplicates

        # Plan - Set approach
        # Using a set to track numbers 
        
        # Create set 
        # loop through nums 
        # if current number is in set, add that 
        #     otherwise return True 
        # break out of loop and return False

        seen = set()

        for n in nums: # iterating over each number
            if n not in seen:
                seen.add(n)
            else:
                return True
        return False