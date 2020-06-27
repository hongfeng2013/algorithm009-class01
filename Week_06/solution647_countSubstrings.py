
# 647. 回文子串
# 给定一个字符串，你的任务是计算这个字符串中有多少个回文子串。
# 具有不同开始位置或结束位置的子串，即使是由相同的字符组成，也会被计为是不同的子串。
# 示例 1:
# 输入: "abc"
# 输出: 3
# 解释: 三个回文子串: "a", "b", "c".
#
# 示例 2:
# 输入: "aaa"
# 输出: 6
# 说明: 6个回文子串: "a", "a", "a", "aa", "aa", "aaa".

class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        if n <= 1:
            return n
        count = 0
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(i):
                dp[j][i] = (s[j] == s[i]) and ((i - j < 2) or dp[j+1][i-1])
                if dp[j][i]:
                    count += 1
            dp[i][i] = 1
            count += 1

        return count
