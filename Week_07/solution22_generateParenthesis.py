
# 22.括号生成
# 数字n代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且有效的括号组合。
#
# 示例：
# 输入：n = 3
# 输出：[
#     "((()))",
#     "(()())",
#     "(())()",
#     "()(())",
#     "()()()"
# ]


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

        backtrack(n, n, track, res)
        return res