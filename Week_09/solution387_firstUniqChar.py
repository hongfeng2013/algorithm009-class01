
# 387.字符串中的第一个唯一字符
# 给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 - 1。
#
# 示例：
# s = "leetcode"
# 返回0
#
# s = "loveleetcode"
# 返回2

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return -1
        dict = {}
        for index, ch in enumerate(s):
            count = dict.setdefault(ch, 0)
            count += 1
            dict[ch] = count
        for index, ch in enumerate(s):
            if dict[ch] == 1:
                return index
        return -1