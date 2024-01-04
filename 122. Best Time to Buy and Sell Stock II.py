class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        i = 0
        k = len(prices)
        total = 0
        while i < k-1:
            if prices[i+1] > prices[i]:
                total += prices[i+1] - prices[i]
                i += 1
            else:
                i += 1
        return total 