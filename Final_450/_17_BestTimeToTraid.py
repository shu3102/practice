class Solution:
    def maxProfit(self, prices):
        max_p = 0
        for i in range(len(prices)):
            t = prices[i]
            for j in range(i + 1, len(prices)):
                if(max_p < (prices[j] - t)):
                    max_p = prices[j] - t
        print(max_p)
        return max_p

class Solution:
    def maxProfit(self, prices):
        minSoFar = prices[0]
        profitSoFar = 0
        
        for i in range(1, len(prices)):
            if((prices[i] - minSoFar) > profitSoFar):
                profitSoFar = prices[i] - minSoFar
            if(minSoFar > prices[i]):
                minSoFar = prices[i]
        return profitSoFar