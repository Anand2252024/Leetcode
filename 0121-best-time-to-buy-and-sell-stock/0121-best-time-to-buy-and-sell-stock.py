from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0
        
        for price in prices:
            # update minimum price
            if price < min_price:
                min_price = price
            # check profit if sold today
            elif price - min_price > max_profit:
                max_profit = price - min_price
        
        return max_profit
