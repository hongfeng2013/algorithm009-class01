
# 给你一个整数数组 nums ，请你找出数组中乘积最大的连续子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。
#
# 示例 1:
# 输入: [2,3,-2,4]
# 输出: 6
# 解释: 子数组 [2,3] 有最大乘积 6。
#
# 示例 2:
# 输入: [-2,0,-1]
# 输出: 0
# 解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。


class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        size = len(nums)
        # dp[x][0]:max, dp[x][1]:min
        dp = [[0] * size for _ in range(2)]
        dp[0][0] = nums[0]
        dp[1][0] = nums[0]
        for i in range(1, size):
            dp[0][i] = max(dp[0][i - 1] * nums[i], nums[i], dp[1][i - 1] * nums[i])
            dp[1][i] = min(dp[0][i - 1] * nums[i], nums[i], dp[1][i - 1] * nums[i])

        return max(dp[0])


nums = [2,3,-2,4]
s1 = Solution()
print(s1.maxProduct(nums))
