
# 121.
# 买卖股票的最佳时机
# 给定一个数组，它的第i个元素是一支给定股票第i天的价格。
# 如果你最多只允许完成一笔交易（即买入和卖出一支股票一次），设计一个算法来计算你所能获取的最大利润。
# 注意：你不能在买入股票前卖出股票。
#
# 示例
# 1:
# 输入: [7, 1, 5, 3, 6, 4]
# 输出: 5
# 解释: 在第2天（股票价格 = 1）的时候买入，在第5天（股票价格 = 6）的时候卖出，最大利润 = 6 - 1 = 5 。
# 注意利润不能是
# 7 - 1 = 6, 因为卖出价格需要大于买入价格；同时，你不能在买入前卖出股票。


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
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
            dp[i][1] = max(dp[i-1][1], -prices[i])
        return dp[n-1][0]