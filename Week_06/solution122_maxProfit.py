
# 122.买卖股票的最佳时机II
# 给定一个数组，它的第i个元素是一支给定股票第i天的价格。
# 设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。
# 注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
#
# 示例
# 1:
# 输入: [7, 1, 5, 3, 6, 4]
# 输出: 7
# 解释: 在第2天（股票价格 = 1）的时候买入，在第3天（股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5 - 1 = 4 。
# 随后，在第4天（股票价格 = 3）的时候买入，在第5天（股票价格 = 6）的时候卖出, 这笔交易所能获得利润 = 6 - 3 = 3 。


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        n = len(prices)
        dp = [[0] * 2 for _ in range(n)]
        dp[0][0] = 0
        dp[0][1] = -prices[0]

        for i in range(1, n):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])

        return dp[n - 1][0]

