
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        res = {}
        for word in strs:
            key = ''.join(sorted(word))
            if key in res:
                res[key].append(word)
            else:
                res[key] = [word]
        return list(res.values())



# input: ["eat", "tea", "tan", "ate", "nat", "bat"]
# output:
# [
#   ["ate","eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ]

l1 = ["eat", "tea", "tan", "ate", "nat", "bat"]
s1 = Solution()
print(s1.groupAnagrams(l1))


