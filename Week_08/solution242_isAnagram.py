
# 242. 有效的字母异位词
# 给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。
#
# 示例 1:
# 输入: s = "anagram", t = "nagaram"
# 输出: true

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        dict_s = {}
        dict_t = {}
        for ch in s:
            dict_s[ch] = dict_s.get(ch, 0) + 1
        for ch in t:
            dict_t[ch] = dict_t.get(ch, 0) + 1

        if dict_s != dict_t:
            return False
        return True