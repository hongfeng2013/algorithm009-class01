
# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4

class Solution:
    def search(self, nums, target):
        if not nums:
            return -1
        l = 0
        r = len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            if nums[m] < nums[r]:
                if target > nums[m] and target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
            else:
                if target >= nums[l] and target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
        return -1

s1 = Solution()
l1 = [4,5,6,7,0,1,2]
target = 3
print(s1.search(l1, target))


