class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Optimal Solution 

        left = 0
        right = len(heights) - 1 
        res = 0 
        while left != right: 
            #calculate the area and take the max area 
            area = (right - left) * min(heights[left], heights[right])
            # update area until we've found max
            res = max(area, res)

            
            if heights[left] < heights[right]: # if left height is the minimum, calculate area and move up by 1
                left += 1 
            elif heights[right] > heights[left]: # if right height is the minimum, calculate area and move down by 1 
                right -= 1 
            else:
                right -= 1
        return res
