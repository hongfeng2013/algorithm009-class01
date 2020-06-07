
#输入: nums = [1,2,3]

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if nums is None:
            return []
        res = []
        track = []
        def backtrack(nums, start, track):
            size = len(nums)
            if start == size:
                res.append(track.copy())
                return

            # 不放nums[i]
            backtrack(nums, start + 1, track)
            # 放nums[i]
            track.append(nums[start])
            backtrack(nums, start + 1, track)
            track.pop()

        backtrack(nums, 0, track)
        return res


s1 = Solution()
nums = [1,2,3]
print(s1.subsets(nums))
