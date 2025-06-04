# LeetCode link: https://leetcode.com/problems/implement-stack-using-queues/description/
# Difficulty: Easy
# Notes: 

# ---------------------------- #

# >>> 1st Attempt <<<
# Time Complexity: 
    # Push: o(n)
    # Pop: o(n)
    # Top: o(1)
    # Empty: o(1)
# Space Complexity:
    # Push: o(n)
    # Pop: o(n)
    # Top: o(n)
    # Empty: o(n)
# Notes:
class MyStack(object):

    def __init__(self):
        self.the_top = [] #Holds top element
        self.rest = [] #Holds everything else (left = top)

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        # Add new value to top queue that 
        self.the_top.append(x)
        # 
        if len(self.the_top) > 1:
            self.rest.append(self.the_top.pop(0))
        

    def pop(self):
        """
        :rtype: int
        """
        if len(self.the_top) > 0:
            res = self.the_top.pop(0)
        
        if len(self.rest) == 0:
            return res
        
        # Move all values to self.rest temporarily
        while len(self.rest) > 0:
            self.the_top.append(self.rest.pop(0))
        
        # Move all but 1 value back to the self.top array
        while len(self.the_top) > 1:
            self.rest.append(self.the_top.pop(0))

        return res
        
    def top(self):
        """
        :rtype: int
        """
        return self.the_top[0]

    def empty(self):
        """
        :rtype: bool
        """
        if len(self.the_top) == 0 and len(self.rest) == 0:
            return True
        return False

# ---------------------------- #

# >>> GPT Dequeue Method <<<
# Time Complexity:
    # Push: o(n)
    # Pop: o(1)
    # Top: o(1)
    # Empty: o(1)
# Space Complexity:
    # Push: o(n)
    # Pop: o(n)
    # Top: o(n)
    # Empty: o(n)
# Notes:
from collections import deque
class MyStack(object):

    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()
        
    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.q2.append(x)
        while self.q1:
            self.q2.append(self.q1.popleft())
        self.q1, self.q2 = self.q2, self.q1

    def pop(self):
        """
        :rtype: int
        """
        return self.q1.popleft()

    def top(self):
        """
        :rtype: int
        """
        return self.q1[0]

    def empty(self):
        """
        :rtype: bool
        """
        if len(self.q1) == 0:
            return True
        return False
# ---------------------------- #

# >>> : <<<
# Time Complexity:
# Space Complexity: 
# Notes:

# ---------------------------- #

# >>> : <<<
# Time Complexity:
# Space Complexity: 
# Notes: