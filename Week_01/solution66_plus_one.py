
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        for i in range(len(digits)-1, -1, -1):
            if digits[i] != 9:
                digits[i] += 1
                return digits
            else:
                digits[i] = 0
        digits.insert(0, 1)
        return digits

    def plusOne2(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        from functools import reduce
        number = reduce(lambda x,y:x*10+y, digits) + 1
        return [int(num) for num in str(number)]


l = [9, 9, 9]
s1 = Solution()
# print(s1.plusOne(l))
print(s1.plusOne2(l))