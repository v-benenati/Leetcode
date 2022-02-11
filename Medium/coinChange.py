class Solution:
    minCoins = {}
    
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        ans =  self.coinChangeHelper(coins, amount)
        print(Solution.minCoins)
        return ans
        
        
    def coinChangeHelper(self, coins, amount):
        if amount < 0:
            return -1
        if amount in coins:
            return 1
        elif amount in Solution.minCoins.keys():
            return Solution.minCoins[amount]
        else:
            currentMin = float(inf)
            for coin in coins:
                afterCoinTaken = self.coinChangeHelper(coins, amount-coin)
                currentAmount = 1+afterCoinTaken
                if currentAmount>-1 and currentAmount < currentMin:
                    currentMin = currentAmount
            
            
            print("Amount:{} Min: {}".format(amount, currentMin))
            Solution.minCoins[amount] = currentMin
            return currentMin
                
         