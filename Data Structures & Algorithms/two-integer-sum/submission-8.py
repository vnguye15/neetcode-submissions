class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # Understand
        # input: nums (list of int), target (int)
        # output: list of indices [i,j] 

        # Plan - Dictionary + Calculate other number (compliment)
        # Take the target - index = compliment
        # If compliment is in nums, return an array where i represents first index, and j represents index of compliment 
        # if compliment isn't in nums, add to dictionary. Value will be index stored 

        # ex: [3,4,5,6], target = 7 
        # i | num
        # 0 | 3
        # 1 | 4
        # 2 | 5
        # 3 | 6 


        # 7 - 3 = 4 --> 3 + 4 = 7. So [0,1] or [0, num[i]]

        # Create dictionary
        # loop through nums
        # calculate compliment
        # if compliment in dictionary: 
        # return [i,nums[compliment]]

        # else compliment not in dictionary:
        # add number with current index associated 

        seen = {}

        for i in range(len(nums)):
            compliment = target - nums[i]
            if compliment in seen:
                return [seen[compliment],i]
            else:
                seen[nums[i]] = i 

        # [3,4,5,6] target = 7
        # seen = {}

        # 3, 7-3 = 4, 4 not in seen --> seen = {3:0} where 3 represents nums[n], 0 represents n
        # 4, 7 - 4 = 3, 3 in seen --> return [0 aka seen[n], 1 aka n] or return [seen[nums[n], n]

            