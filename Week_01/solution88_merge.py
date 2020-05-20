
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        index1 = 0
        index2 = 0
        new_list = nums1[:m]
        nums1[:] = []
        while index1 < m and index2 < n:
            if new_list[index1] <= nums2[index2]:
                nums1.append(new_list[index1])
                index1 += 1
            else:
                nums1.append(nums2[index2])
                index2 += 1

        if index1 >= m:
            for i in range(index2, n):
                nums1.append(nums2[i])
        if index2 >= n:
            for i in range(index1, m):
                nums1.append(new_list[i])


l1 = [1, 3, 6, 10]
l2 = [2, 6, 7, 8, 9]
s1 = Solution()
s1.merge(l1, 4, l2, 5)
print(l1)


