class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        # Understand
        # Can numbers repeat? 

        # Ex: [1,2,3,4], target = 3 
        #      L     R 

        # 1 + 4 = 5 > 3: Decrease R by 1 
        # 1 + 3 = 4 > 3: Dec. R by 1 
        # 1 + 2 = 3 == 3: return index position 1 and index position 2 
        # [1,2] where 1 represents first index, and 2 represents second index 

        

        # Plan
        # Approach: Use 2 pointers and increase/decrement left/right pointers until 
        # left + right == target 

        left = 0
        right = len(numbers) - 1 

        while left < right: 
            if numbers[left] + numbers[right] == target:
                return [left + 1, right + 1]
            elif numbers[left] + numbers[right] >= target:
                right -= 1 
            else:
                left += 1 
        
