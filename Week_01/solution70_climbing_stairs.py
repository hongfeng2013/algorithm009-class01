
class Solution(object):
    def climbStairs(self, n):
        method = list(range(n + 1))
        if n == 1:
            return 1
        if n == 2:
            return 2
        method[1] = 1
        method[2] = 2

        for i in range(3, n + 1):
            method[i] = method[i - 1] + method[i - 2]

        return method[n]