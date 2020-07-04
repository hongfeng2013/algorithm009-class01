
# 36. 有效的数独
# 判断一个 9x9 的数独是否有效。只需要根据以下规则，验证已经填入的数字是否有效即可。
#
# 数字 1-9 在每一行只能出现一次。
# 数字 1-9 在每一列只能出现一次。
# 数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。


class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        from collections import defaultdict
        row = defaultdict(set)
        col = defaultdict(set)
        square = defaultdict(set)

        m = len(board)
        n = len(board[0])
        for i in range(m):
            for j in range(n):
                if board[i][j] != '.':
                    if board[i][j] in row[i]:
                        return False
                    if board[i][j] in col[j]:
                        return False
                    if board[i][j] in square[(i//3, j//3)]:
                        return False
                    row[i].add(board[i][j])
                    col[j].add(board[i][j])
                    square[(i//3, j//3)].add(board[i][j])
        return True

