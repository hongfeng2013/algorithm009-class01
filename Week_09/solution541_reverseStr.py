# 541.反转字符串II
# 给定一个字符串s和一个整数k，你需要对从字符串开头算起的每隔2k个字符的前k个字符进行反转。
#
# 如果剩余字符少于k个，则将剩余字符全部反转。如果剩余字符小于2k但大于或等于k个，则反转前
# k个字符，其余字符保持原样。
#
# 示例:
# 输入: s = "abcdefg", k = 2
# 输出: "bacdfeg"


class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        flag = True
        res = ""
        for i in range(0, len(s), k):
            res += s[i:i+k][::-1] if flag else s[i:i+k]
            flag = not flag
        return res