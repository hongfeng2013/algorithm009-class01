
# 188. 买卖股票的最佳时机 IV
# 给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。
#
# 设计一个算法来计算你所能获取的最大利润。你最多可以完成 k 笔交易。
#
# 注意: 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
#
# 示例 1:
#
# 输入: [2,4,1], k = 2
# 输出: 2
# 解释: 在第 1 天 (股票价格 = 2) 的时候买入，在第 2 天 (股票价格 = 4) 的时候卖出，这笔交易所能获得利润 = 4-2 = 2 。
# 示例 2:
#
# 输入: [3,2,6,5,0,3], k = 2
# 输出: 7
# 解释: 在第 2 天 (股票价格 = 2) 的时候买入，在第 3 天 (股票价格 = 6) 的时候卖出, 这笔交易所能获得利润 = 6-2 = 4 。
#      随后，在第 5 天 (股票价格 = 0) 的时候买入，在第 6 天 (股票价格 = 3) 的时候卖出, 这笔交易所能获得利润 = 3-0 = 3 。


class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        def maxProfit_k_inf(prices):
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

        n = len(prices)
        if n <= 1:
            return 0

        if k > n - 1:
            return maxProfit_k_inf(prices)

        dp = [[[0] * 2 for j in range(k+1)] for _ in range(n)]

        for i in range(0, n):
            dp[i][0][0] = 0
            dp[i][0][1] = float('-INF')

        for j in range(0, k+1):
            dp[0][j][0] = 0
            dp[0][j][1] = -prices[0]

        for i in range(1, n):
            for j in range(1, k+1):
                dp[i][j][0] = max(dp[i-1][j][0], dp[i-1][j][1] + prices[i])
                dp[i][j][1] = max(dp[i-1][j][1], dp[i-1][j-1][0] - prices[i])

        return dp[n-1][k][0]