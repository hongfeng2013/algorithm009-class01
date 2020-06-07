
class Solution:
    def permute(self, nums):

        res = []
        track = []

        def backtrack(nums, track):
            if len(track) == len(nums):
                res.append(track[:])
                return
            for i in range(len(nums)):
                if nums[i] in track:
                    continue
                track.append(nums[i])
                backtrack(nums, track)
                track.pop()

        backtrack(nums, track)
        return res

s1 = Solution()
l1 = [1,2,3]
print(s1.permute(l1))
