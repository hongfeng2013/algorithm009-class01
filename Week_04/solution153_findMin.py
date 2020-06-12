
# 输入: [3,4,5,1,2]
# 输出: 1

class Solution:
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if left == right:
                return nums[left]
            # min is in left
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        return nums[left]

l1 = [3,4,5,1,2]
s1 = Solution()
print(s1.findMin(l1))
