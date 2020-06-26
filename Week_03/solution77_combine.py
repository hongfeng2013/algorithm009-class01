
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        res = []
        track = []

        def backtrack(n, k, start, track):
            if k == len(track):
               res.append(track)
               return

            for i in range(start, n+1):
                track.append(i)
                backtrack(n, k, i+1, track)
                track.pop()

        backtrack(n, k, 1, track)
        return res
