
# 130. 被围绕的区域
# 给定一个二维的矩阵，包含 'X' 和 'O'（字母 O）。
# 找到所有被 'X' 围绕的区域，并将这些区域里所有的 'O' 用 'X' 填充。
#
# 示例:
# X X X X
# X O O X
# X X O X
# X O X X
# 运行你的函数后，矩阵变为：
# X X X X
# X X X X
# X X X X
# X O X X


class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        m = len(board)
        n = len(board[0])
        if m < 3 or n < 3:
            return

        def dfs(i, j):
            if board[i][j] == 'O':
                board[i][j] = '#'
            else:
                return
            dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
            for dir in dirs:
                new_i = i + dir[0]
                new_j = j + dir[1]
                if 0 <= new_i < m and 0 <= new_j < n and board[new_i][new_j] == 'O':
                    dfs(new_i, new_j)

        # 第0/m行
        for i in range(n):
            dfs(0, i)
            dfs(m-1, i)

        for i in range(m):
            dfs(i, 0)
            dfs(i, n-1)

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == '#':
                    board[i][j] = 'O'