
class Solution(object):
    def climbStairs(self, n):
        def climb_stairs(n):
            if n == 1:
                return 1
            if n == 2:
                return 2
            return climb_stairs(n-1) + climb_stairs(n-2)

        return climb_stairs(n)

    def climbStairs2(self, n):
        if n == 1:
            return 1
        if n == 2:
            return 2
        f = {}
        f[1] = 1
        f[2] = 2
        for i in range(3, n+1):
            f[i] = f[i-1] + f[i-2]
        return f[n]


s1 = Solution()
print(s1.climbStairs(4))
print(s1.climbStairs2(4))