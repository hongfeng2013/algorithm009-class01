
# 200.岛屿数量
# 给你一个由'1'（陆地）和'0'（水）组成的的二维网格，请你计算网格中岛屿的数量。
# 岛屿总是被水包围，并且每座岛屿只能由水平方向或竖直方向上相邻的陆地连接形成。
# 此外，你可以假设该网格的四条边均被水包围。
#
# 示例
# 1:
# 输入:
# [
#     ['1', '1', '1', '1', '0'],
#     ['1', '1', '0', '1', '0'],
#     ['1', '1', '0', '0', '0'],
#     ['0', '0', '0', '0', '0']
# ]
# 输出: 1

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        m = len(grid)
        n = len(grid[0])
        count = 0

        def dfs(i, j):
            grid[i][j] = '0'
            dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
            for dir in dirs:
                new_i = i + dir[0]
                new_j = j + dir[1]
                if 0 <= new_i < m and 0 <= new_j < n and grid[new_i][new_j] == '1':
                    dfs(new_i, new_j)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    count += 1
                    dfs(i, j)
        return count