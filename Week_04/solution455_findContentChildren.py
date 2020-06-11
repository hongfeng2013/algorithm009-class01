
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        gi = 0
        si = 0
        res = 0

        while gi < len(g) and si < len(s):
            if s[si] >= g[gi]:
                si += 1
                gi += 1
                res += 1
            else:
                si += 1
        return res

    def findContentChildren2(self, g: List[int], s: List[int]) -> int:
        import heapq
        heapq.heapify(g)
        heapq.heapify(s)

        res = 0
        while g and s:
            if s[0] >= g[0]:
                heapq.heappop(g)
                heapq.heappop(s)
                res += 1
            else:
                heapq.heappop(s)
        return res
