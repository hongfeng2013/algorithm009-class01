
class Solution(object):
    # 暴力法
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_area = 0
        size = len(height)
        for i in range(0, size-1):
            for j in range(0, size):
                area = (j-i) * min(height[i], height[j])
                max_area = max(max_area, area)

        return max_area

    def maxArea2(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_area = 0
        i = 0
        j = len(height) - 1
        while i < j:
            area = (j - i) * min(height[i], height[j])
            max_area = max(max_area, area)
            if height[i] <= height[j]:
                i += 1
            else:
                j -= 1
        return max_area


l = [1,8,6,2,5,4,8,3,7]
s1 = Solution()
print(s1.maxArea(l))
print(s1.maxArea2(l))
