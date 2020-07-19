# 917.仅仅反转字母
# 给定一个字符串
# S，返回 “反转后的” 字符串，其中不是字母的字符都保留在原地，而所有字母的位置发生反转。
#
# 示例1：
# 输入："ab-cd"
# 输出："dc-ba"
# 示例2：
# 输入："a-bC-dEf-ghIj"
# 输出："j-Ih-gfE-dCba"


class Solution(object):
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        start = 0
        end = len(S) - 1
        S = list(S)
        while start < end:
            if not S[start].isalpha():
                start += 1
            elif not S[end].isalpha():
                end -= 1
            else:
                S[start], S[end] = S[end], S[start]
                start += 1
                end -= 1

        return "".join(S)