
# 213. 打家劫舍 II
# 你是一个专业的小偷，计划偷窃沿街的房屋，每间房内都藏有一定的现金。这个地方所有的房屋都围成一圈，这意味着第一个房屋和最后
# 一个房屋是紧挨着的。同时，相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。
#
# 给定一个代表每个房屋存放金额的非负整数数组，计算你在不触动警报装置的情况下，能够偷窃到的最高金额。
#
# 示例 1:
#
# 输入: [2,3,2]
# 输出: 3
# 解释: 你不能先偷窃 1 号房屋（金额 = 2），然后偷窃 3 号房屋（金额 = 2）, 因为他们是相邻的。


class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def rob_range(nums, start, end):
            # 0:不偷， 1：偷
            dp = [[0] * 2 for _ in range(end-start+1)]
            dp[0][0] = 0
            dp[0][1] = nums[start]
            for i in range(1, end-start+1):
                dp[i][0] = max(dp[i-1][0], dp[i-1][1])
                dp[i][1] = max(dp[i-1][0] + nums[i+start], dp[i-1][1])
            return max(dp[end-start][0], dp[end-start][1])

        if not nums:
            return 0
        size = len(nums)
        if size == 1:
            return nums[0]
        return max(rob_range(nums, 0, size-2), rob_range(nums, 1, size-1))