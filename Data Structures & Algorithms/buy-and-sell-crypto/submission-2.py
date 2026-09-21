class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # Understand
        # input: prices (list of int)
        # output: Maximum profit (int)

        # Profit = Sell - Buy
        # Choose a SINGLE DAY to buy, and a DIFFERENT DAY in FUTURE to sell

        # Rules: if the sell price is < buy, disregard current number
        # [10,1,5,6,7,1] 
        # Buy = 10, Sell = 1,5,6, etc.. Sell < Buy spotted so move up 1 for buy
        # Buy = 1, Sell = 5,6,7,1... max(Sell - Buy) = (5-1,6-1,7-1,1-1), max(Sell-Buy) = 6
        # Buy = 5, Sell = 6,7,1...  Sell < Buy spotted so move up 1 for Buy 
        # Buy = 6, Sell = 7,1 ... 

        # Plan - Sliding Window Approach
        # create a buy (left) pointer
        # create a sell (right pointer)
        # create a profit 
        # create a max profit 

        # Loop through prices
        # when Sell < Buy, move Buy to a different day by 1 
        # calculate profit, and take the max profit calculated to track maximum profit 
        # Sell always moves to a different day


        buy = 0 
        sell = 1 # always start sell at another day (future day)
        profit = 0 
        maxProfit = 0

        # [10,1,5,6]
        #       B
        #       S       

        # sell = 0
        # buy = 0

        while sell < len(prices):
            if prices[sell] < prices[buy]: 
                buy = sell
            else:
                profit = prices[sell] - prices[buy]
                maxProfit = max(maxProfit, profit)
            sell += 1
        return maxProfit


