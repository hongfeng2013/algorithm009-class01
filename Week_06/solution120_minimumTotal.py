
# 三角形最小路径和
# 给定一个三角形，找出自顶向下的最小路径和。每一步只能移动到下一行中相邻的结点上。
#
# 相邻的结点在这里指的是下标与上一层结点下标
# 相同或者等于上一层结点下标 + 1的两个结点.
#
# 例如，给定三角形：
#
# [
#     [2],
#     [3, 4],
#     [6, 5, 7],
#     [4, 1, 8, 3]
# ]
# 自顶向下的最小路径和为
# 11（即，2 + 3 + 5 + 1 = 11）。

class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        m = len(triangle)
        n = len(triangle[-1])
        dp = [[0] * n for _ in range(m)]
        for i in range(n):
            dp[m-1][i] = triangle[m-1][i]

        for i in range(m-2, -1, -1):
            for j in range(i+1):
                dp[i][j] = min(dp[i+1][j], dp[i+1][j+1]) + triangle[i][j]

        return dp[0][0]