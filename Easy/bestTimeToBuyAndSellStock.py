class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        runningMax = [0]*len(prices)
        currMax = prices[-1]
        for index in range(len(prices)):
            day = len(prices)-1-index 
            price = prices[day]
            if currMax < price:
                currMax = price
            runningMax[day] = currMax
        print(runningMax)
        maxProfit = 0
        for day, price in enumerate(prices):
            profit = runningMax[day]-price
            if profit > maxProfit:
                maxProfit = profit
                
        return maxProfit