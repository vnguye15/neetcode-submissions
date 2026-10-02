class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # Understand
        # input: prices (list of ints)
        # output: profit (prices[i] --> int)

        # choose single day to buy, and different day to sell
        #   meaning: Buy comes first, sell always comes after
        
        # Edge cases:
        # What happens if profit (sell - buy) = negative or 0? 
        # prices = [] (no transaction) --> profit = 0 

        # Plan - 2 Pointer approach
        
        # (Edge Case)
        # if prices array empty:
        #  return 0 

        # create left and right pointers (right always moves)
        # create a max profit (stores profit)
        # loop through prices 
        # if Sell > Buy:
        #   calculate profit 
        #   save and update to max profit variable 
        # else: 
        #  move left pointer by 1 

        # break out of loop and return profit 

        buy = 0
        maxProfit = 0 
        sell = 1

        if len(prices) == 0:
            return 0

        while sell <= len(prices) - 1:
            if prices[sell] > prices[buy]:
                profit = prices[sell] - prices[buy]
                maxProfit = max(maxProfit, profit)
            else:
                buy = sell
            sell += 1 
        return maxProfit


        # prices=[7,1,5,3,6,4]
        
        # output: 4 
        # expected: 5 

        # buy = 7, sell = 1
