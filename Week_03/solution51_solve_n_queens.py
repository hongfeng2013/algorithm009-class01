
# @lc code=start
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.'] * n for _ in range(n)]

        res = []
        cols = set()
        master = set()
        slave = set()
        from copy import deepcopy
        def backtrace(row):
            def is_valid(row, col):
                if col in cols or row + col in master or row - col in slave:
                    return False
                return True

            if row == n:
                board2 = []
                for row in board:
                    board2.append(''.join(row))
                res.append(deepcopy(board2))
                return
            for col in range(n):
                if not is_valid(row, col):
                    continue

                board[row][col] = 'Q'
                cols.add(col)
                master.add(row + col)
                slave.add(row - col)
                backtrace(row + 1)
                board[row][col] = '.'
                cols.remove(col)
                master.remove(row + col)
                slave.remove(row - col)

        backtrace(0)
        return res


