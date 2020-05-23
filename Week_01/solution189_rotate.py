
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        size = len(nums)
        k = k % size
        if k == 0:
            return
        for i in range(0, k):
            last = nums[-1]
            for j in range(0, size):
                nums[j], last = last, nums[j]

    def rotate2(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        size = len(nums)
        k = k % size
        if k == 0:
            return

        nums[:-k], nums[-k:] = nums[-k:], nums[:-k]
