class MinStack(object):

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)
        
        if not self.minStack:
            self.minStack.append(val)
        else:
            self.minStack.append(min(self.minStack[-1], val))
        

    def pop(self):
        """
        :rtype: None
        """
        self.minStack.pop()
        self.stack.pop()
        

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.minStack[-1]
        