#/usr/bin/python

class Solution(object):
    def moveZeroes(self, nums):
        j = 0
        for i in nums:
            if i != 0:
                nums[j] = i
                j += 1

        for i in range(j, len(nums)):
            nums[i] = 0
        return nums
