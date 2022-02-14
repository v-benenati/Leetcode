class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        return self.coinChangeHelper(coins, amount, memo={})
        
        
        
    def coinChangeHelper(self, coins, amount, memo={}):
        if amount < 0:
            return -1
        if amount == 0:
            return 0
        if amount in coins:
            return 1
        elif amount in memo:
            return memo[amount]
        else:
            currentMin = float(inf)
            for coin in coins:
                afterCoinTaken = self.coinChangeHelper(coins, amount-coin, memo)
                currentAmount = 1+afterCoinTaken
                if afterCoinTaken>-1 and currentAmount < currentMin:
                    currentMin = currentAmount
            
            if currentMin == float(inf):
                currentMin = -1
            
            memo[amount] = currentMin
            return currentMin
                
         