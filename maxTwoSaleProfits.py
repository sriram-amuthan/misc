# Question: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        result = 0
        if n < 2:
            return result
        # leftMaxSell[i] = maxSell(prices[:i]))
        leftMaxSell = self.getLeftMaxSell(prices)
        # rightMaxSell[i] = maxSell(prices[i:])
        rightMaxSell = self.getRightMaxSell(prices)
        for sep in range(n + 1):
            result = max(result, leftMaxSell[sep] + rightMaxSell[sep])
        return result
    
    def getLeftMaxSell(self, prices):
        n = len(prices)
        if n < 2:
            return 0
        localMax, localMin, maxProfit, profits = prices[0],prices[0],0,[0]*(n+1)
        for i in range(n+1):
            if i == n: #Handle the 
                maxProfit = max(maxProfit, localMax - localMin)
                profits[i] = maxProfit
                break
            if prices[i] < localMin:
                maxProfit = max(maxProfit, localMax - localMin)
                localMin = prices[i]
                localMax = localMin # Reset localMax
            if prices[i] > localMax:
                localMax = prices[i]
                maxProfit = max(maxProfit, localMax - localMin)
            profits[i] = maxProfit
        return profits
    
    def getRightMaxSell(self, prices):
        n = len(prices)
        if n < 2:
            return 0
        localMax, localMin, maxProfit, profits = prices[-1],prices[-1],0,[0]*(n+1)
        for i in range(n-1, -1, -1):
            if prices[i] > localMax:
                maxProfit = max(maxProfit, localMax - localMin)
                localMax = prices[i]
                localMin = localMax # Reset localMin
            if prices[i] < localMin:
                localMin = prices[i]
                maxProfit = max(maxProfit, localMax - localMin)
            profits[i] = maxProfit
        return profits
