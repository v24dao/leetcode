# LeetCode link:
# Difficulty:
# Notes: 

# ---------------------------- #

# >>> My solution <<<
# Time Complexity: 
# Space Complexity:
# Notes:
class MyQueue(object):
    # Stack a: contains all elements (in queue order)
    # Stack b: temporary/dummy stack, used only for pop/peak operations.

    # When elements are in a, the are in queue order:
        # [1,2,3,...]
    # while elements are in b, they are in reverse queue order:
        # [...,3,2,1]
    
    def __init__(self):
        self.a = []
        self.b = []       

    # Keep adding to the end of a.
    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.a.append(x)

    # Pop from a into b until we have ONE element left in a.
    # The remaining element in a is the front of our queue. Deal with it accordingly for 'pop' and 'peak' operations.
    # Pop all elements from b, placing them back into a.

    def pop(self):
        """
        :rtype: int
        """
        while len(self.a) > 1:
            self.b.append(self.a.pop())
        res = self.a.pop()
        while len(self.b) > 0:
            self.a.append(self.b.pop())
        return res

    def peek(self):
        """
        :rtype: int
        """
        while len(self.a) > 1:
            self.b.append(self.a.pop())
        res = self.a[0]
        while len(self.b) > 0:
            self.a.append(self.b.pop())
        return res

    def empty(self):
        """
        :rtype: bool
        """
        if self.a:
            return False
        return True
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

# ---------------------------- #

# >>> : <<<
# Time Complexity:
# Space Complexity: 
# Notes: