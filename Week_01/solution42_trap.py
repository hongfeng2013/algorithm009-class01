
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # 暴力法
        size = len(height)
        res = 0
        for i in range(1, size):
            left_max = 0
            right_max = 0
            for j in range(i, -1, -1):
                left_max = max(left_max, height[j])
            for j in range(i, size, 1):
                right_max = max(right_max, height[j])

            res += min(left_max, right_max) - height[i]

        return res

    def trap2(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        #双指针
        left = 0
        right = len(height) - 1
        res = 0
        left_max, right_max = 0, 0
        while left < right:
            if height[left] < height[right]:
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    res += left_max - height[left]
                left += 1
            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    res += right_max - height[right]
                right -= 1

        return res

    def trap3(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        #stack
        size = len(height)
        if size < 3:
            return 0
        res = 0
        stack = []

        for i in range(0, size):
            while len(stack) > 0 and height[i] > height[stack[-1]]:
                top = stack.pop()
                if len(stack) == 0:
                    break
                h = min(height[i], height[stack[-1]]) - height[top]
                distance = i - stack[-1] - 1
                res += h * distance

            stack.append(i)
        return res



l = [0,1,0,2,1,0,1,3,2,1,2,1]
s1 = Solution()
print(s1.trap2(l))
print(s1.trap3(l))





