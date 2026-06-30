class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        mini=prices[0]
        for i in range(1,len(prices)):
            cost=prices[i]-mini
            profit=max(profit,cost)
            mini=min(mini,prices[i])
        return profit
    
    """ TC=O(n) SC=O(1)
    return the maximum profit that can be achieved by buying and selling the stock represented by the array"""