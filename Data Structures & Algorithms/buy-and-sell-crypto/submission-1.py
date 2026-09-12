class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # Plan
        # set up left and right pointer (sliding window)
        # create a variable to track max profit 
        # move left + right pointer over until we've hit a profit/positive number (sell - buy = positive number)
        # once profit returns positive number, only move right pointer 
        # update profit as we go along 

        left = 0  # left (buy)
        right = 1 # right (sell), 
        maxProfit = 0 #profit = right - left (sell - buy)

        while right < len(prices): # move right pointer over while it hasn't passed last price point
            # checking if profit was made:
            if prices[left] < prices[right]: # want buy price to be less than sell price 
                profit = prices[right] - prices[left] # calculate profit 
                maxProfit = max(maxProfit, profit) # return whatever 
            else: # otherwise no profit, so update left pointer and right pointer over 
                left = right # we want left pointer to always start at the minimum, this ensures it 
            right += 1 # ALWAYS move right pointer over 1 
        return maxProfit
            


            # shift left pointer TO right pointer (will guarantee we start left at minimum)
        