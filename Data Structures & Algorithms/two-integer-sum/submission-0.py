class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # result_array =[]
        # complementary = target - nums[0]
        # result_array.append(nums[0])
        # for index in range(len(nums)):
        #     if index == complementary:
        #         result_array.append(nums[index])
        # return result_array

        
    
    # nums = [3,4,5,6], target = 7
    # output: [0,1]

    # Understand
    # one thing i've noticed is that the nums[0] is always included in output 
    # Equation: nums[i] + nums[j] == target
    # Rearranged: nums[j] == target - nums[i] (finds complementary) 
    # Example: nums[1] == 7 - nums[0] --> 3 = 7 - 4 

    # Plan
    # Create result array 
    # Find nums[j] or complementary with rearranged equation
    # add first element or nums[0] to result array
    # loop through array length via range to generate our index values (0,1,2,3)
    # if element matches with nums[j] {add nums[j] to result array}
    # break out of loop and return the result array  

    #Neetcode solution:
        prevMap = {} #val : index

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
    



   