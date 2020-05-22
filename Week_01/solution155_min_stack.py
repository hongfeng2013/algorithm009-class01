
class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.normal_stack = []
        self.min_stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if len(self.min_stack) != 0:
            if x < self.min_stack[-1]:
                self.min_stack.append(x)
            else:
                self.min_stack.append(self.min_stack[-1])
        else:
            self.min_stack.append(x)
        self.normal_stack.append(x)

    def pop(self):
        """
        :rtype: None
        """
        self.min_stack.pop()
        return self.normal_stack.pop()

    def top(self):
        """
        :rtype: int
        """
        if len(self.normal_stack) != 0:
            return self.normal_stack[-1]
        else:
            return None

    def getMin(self):
        """
        :rtype: int
        """
        if len(self.min_stack) != 0:
            return self.min_stack[-1]
        else:
            return None


