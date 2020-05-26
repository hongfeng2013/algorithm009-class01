
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # 排序并比较
        if len(s) != len(t):
            return False
        if sorted(s) != sorted(t):
            return False
        return True

    def isAnagram2(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # map并比较
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


s = "anagram"
t = "nagaram"
s1 = Solution()
print(s1.isAnagram(s, t))
print(s1.isAnagram2(s, t))