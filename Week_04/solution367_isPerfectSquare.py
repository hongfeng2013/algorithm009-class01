
# 示例 1：
# 输入：16
# 输出：True
#
# 示例 2：
# 输入：14
# 输出：False

class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 0:
            return True
        left = 0
        right = num
        while left <= right:
            mid = (left + right) // 2
            if mid * mid == num:
                return True
            elif mid * mid < num:
                left = mid + 1
            else:
                right = mid - 1
        return False