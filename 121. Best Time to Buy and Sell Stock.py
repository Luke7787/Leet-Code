class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        i = 0
        k = len(prices)
        min = prices[0]
        total = 0
        while i < k:
            if prices[i] < min:
                min = prices[i]
            elif prices[i] - min >= total:
                total = prices[i] - min
                i += 1
            else:
                i += 1
        return total