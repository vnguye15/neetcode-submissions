class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Optimized Solution

        Understand
        input: nums (list) and target (int)
        Want: list of indices that add up to target 

        Ex: [3,4,5,6] and target = 7 

        - Find the difference and grab the index of the difference + index of current number that both add up to 7 
        
        i = 0, n = 3: diff = target - n, diff = 7 - 3, diff = 4, 

        diff not seen in map so add (i=0,n=3) to map --> [(0:3), ]
        
        Plan

        Create python dict prevSeen with num:index pair 
        Iterate through nums list
        Calculate diff at each iteration 
        if diff is in prevSeen:
            return array with corresponding 2 indices
        otherwise add val:index pair to prevSeen 
        """

        prevSeen = {}
        for i, n in enumerate(nums):
            diff = target - n 
            if diff in prevSeen:
                return [prevSeen[diff], i] 
            else:
                prevSeen[n] = i



