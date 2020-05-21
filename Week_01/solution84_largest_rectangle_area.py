
class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        # 暴力法
        size = len(heights)
        heights = [0] + heights + [0]
        size += 2
        res = 0
        for i in range(1, size):
            left = i
            right = i
            for j in range(i-1, -1, -1):
                if heights[j] < heights[i]:
                    left = j
                    break
            for j in range(i+1, size, 1):
                if heights[j] < heights[i]:
                    right = j
                    break
            area = heights[i] * (right - left -1)
            res = max(res, area)

        return res

    def largestRectangleArea2(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        # use stack
        size = len(heights)
        heights = [0] + heights + [0]
        size += 2
        stack = []
        res = 0

        for i in range(0, size):
            while len(stack) > 0 and heights[i] < heights[stack[-1]]:
                height = heights[stack.pop()]
                width = i - stack[-1] - 1
                res = max(res, height*width)
            stack.append(i)
        return res


l1 = [2,1,5,6,2,3]
# l1 = [2]
s1 = Solution()
print(s1.largestRectangleArea(l1))
print(s1.largestRectangleArea2(l1))
