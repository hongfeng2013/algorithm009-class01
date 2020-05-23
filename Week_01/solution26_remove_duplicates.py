
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size = len(nums)
        if size <= 1:
            return size

        i = 0
        for j in range(1, size):
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]

        return i+1