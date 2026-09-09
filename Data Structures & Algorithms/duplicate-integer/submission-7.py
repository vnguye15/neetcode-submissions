class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        # Understand
        # input: nums (list of integers)
        # output: true/false (boolean)


        # 0 <= nums.length <= 10^5 --> hashmap 

        # Scenario:
        
        # nums = [1,2,3,3] 
        # 3 appears @ i=2 and i=3 --> duplicate found (value appears at 2 different index)

        # nums = [1,2,3,4]
        # no duplicate found (value appears at 1 index only)

        # Plan
        # Create a python set to track and store unique values
        # loop through nums list 
        # if current element (value) not found in set:
        #  add to set 
        # otherwise duplicate found, return True

        # break out of loop, no duplicate found, return False

        seen = set()
        for num in nums: # for each number in nums
            if num in seen: # if number has already appeared in set
                return True # return True 
            seen.add(num) # Failing Test Case #2 @ line 32 | Plan to Switch True and False
        return False


        

