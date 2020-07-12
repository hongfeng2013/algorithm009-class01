
# 231. 2的幂
# 给定一个整数，编写一个函数来判断它是否是 2 的幂次方。
# 示例 1:
# 输入: 1
# 输出: true
# 解释: 20 = 1

class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n != 0 and (n & (n - 1)) == 0:
            return True
        return False