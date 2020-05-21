
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict = {}
        for i in range(len(nums)):
            num1 = nums[i]
            num2 = target - num1
            if num2 in dict:
                return [dict[num2], i]
            else:
                dict[nums[i]] = i
        return []


nums = [2, 7, 11, 15]
target = 18
s1 = Solution()
print(s1.twoSum(nums, target))