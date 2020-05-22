
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dict1 = {'(': ')', '[': ']', '{': '}'}
        stack = []

        for ch in s:
            if ch in dict1:
                stack.append(dict1[ch])
            else:
                if len(stack) == 0:
                    return False
                else:
                    if ch != stack.pop():
                        return False

        if len(stack) != 0:
            return False
        else:
            return True
