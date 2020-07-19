# 151.翻转字符串里的单词
# 给定一个字符串，逐个翻转字符串中的每个单词。
#
# 示例1：
# 输入: "the sky is blue"
# 输出: "blue is sky the"
# 示例2：
# 输入: "  hello world!  "
# 输出: "world! hello"
# 解释: 输入字符串可以在前面或者后面包含多余的空格，但是反转后的字符不能包括。


class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = s.split()
        return " ".join(words[::-1])