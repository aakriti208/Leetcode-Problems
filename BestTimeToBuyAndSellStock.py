class Solution:
    def maxProfit(self, prices):
        # First we assign a mininum price, which is infinity
        min_price = float(inf)
        # We assign the maximum profit we have so far, which is at 0
        max_profit = 0

        # We go through each price in the list
        for price in prices:
            # If any of the price is less than the minimum price we have,
            # we replace the minimum price with the current price
            if price < min_price:
                min_price = price

            # We calculate the profit, which is the difference between 
            # the current price we're looking at and the minimum price we have
            profit = price - min_price

            # We check to see if the profit we got is greater than the 
            # maximim profit we currently have, and replace it
            if profit > max_profit:
                max_profit = profit
            
        return max_profit
    
    # Space complexity : O(1)
    # Time complexity : O(n) 

