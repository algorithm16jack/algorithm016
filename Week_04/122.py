class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <= 1:
            return 0
        min_value = prices[0]
        total_diff = 0
        for i in range(1, len(prices)):
            if prices[i] < prices[i - 1] and prices[i - 1] > min_value:
                total_diff += (prices[i - 1] - min_value)
                min_value = prices[i]
            if prices[i] < min_value:
                min_value = prices[i]
            if i == len(prices) - 1:
                if prices[i] - min_value > 0:
                    total_diff += (prices[i] - min_value)
        
        return total_diff
