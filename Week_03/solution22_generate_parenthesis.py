
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        if n == 0:
            return []
        res = []
        track = ''

        def backtrack(left, right, track, res):
            if left > right:
                return
            if left < 0 or right < 0:
                return
            if left == 0 and right == 0:
                res.append(track)
                return

            track += '('
            backtrack(left-1, right, track, res)
            track = track[:-1]

            track += ')'
            backtrack(left, right-1, track, res)
            track = track[:-1]

        backtrack(n, n, track, res)
        return res

n = 3
s1 = Solution()
print(s1.generateParenthesis(n))

# 输入：n = 3
# 输出：[
#        "((()))",
#        "(()())",
#        "(())()",
#        "()(())",
#        "()()()"
#      ]

