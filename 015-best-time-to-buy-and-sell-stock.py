class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP, minP = 0, prices[0]
        
        for i in range(1, len(prices)):
            maxP = max(maxP, prices[i] - minP)
            minP = min(minP, prices[i])
            
        return maxP
            