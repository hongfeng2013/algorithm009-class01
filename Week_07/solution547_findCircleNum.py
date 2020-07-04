
# 547. 朋友圈
# 班上有 N 名学生。其中有些人是朋友，有些则不是。他们的友谊具有是传递性。如果已知 A 是 B 的朋友，B 是 C 的朋友，那么我们可以认
# 为 A 也是 C 的朋友。所谓的朋友圈，是指所有朋友的集合。
#
# 给定一个 N * N 的矩阵 M，表示班级中学生之间的朋友关系。如果M[i][j] = 1，表示已知第 i 个和 j 个学生互为朋友关系，否则为不知
# 道。你必须输出所有学生中的已知的朋友圈总数。
#
# 示例 1:
# 输入:
# [[1,1,0],
#  [1,1,0],
#  [0,0,1]]
# 输出: 2
# 说明：已知学生0和学生1互为朋友，他们在一个朋友圈。
# 第2个学生自己在一个朋友圈。所以返回2。


class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        if not M:
            return 0
        n = len(M)
        count = 0
        visited = set()

        def dfs(i):
            for j in range(n):
                if M[i][j] == 1 and j not in visited:
                    visited.add(j)
                    dfs(j)

        for i in range(n):
            if i not in visited:
                count += 1
                dfs(i)
        return count
