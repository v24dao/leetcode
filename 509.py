# LeetCode link:
# Difficulty: Easy
# Notes: FIBONACCI

# ---------------------------- #

# >>> Recursive Method <<<
# Time Complexity: O(2^n) 
# very inefficient! -> for each call, you are making 2 more calls. 2x2x2..etc
# There is a binary tree with REPEATED calculations!

# Space Complexity: O(n)
# -> In the worst case, each callstack goes down to fib(0)
# Notes:
class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 1:
            return n
        
        return self.fib(n-2) + self.fib(n-1)

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