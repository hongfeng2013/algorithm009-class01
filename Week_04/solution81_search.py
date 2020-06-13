

# 输入: nums = [2,5,6,0,0,1,2], target = 0
# 输出: true

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        if not nums:
            return False
        left = 0
        right = len(nums) - 1
        while left <= right:
            while left < right and nums[left] == nums[right]:
                left += 1
            mid = (left + right) // 2
            if nums[mid] == target:
                return True
            elif nums[mid] >= nums[left]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            elif nums[mid] <= nums[right]:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return False

l1 = [2,5,6,0,0,1,2]
s1 = Solution()
print(s1.search(l1, 0))
