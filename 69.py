# LeetCode link:
# Difficulty: Easy
# Notes: 

# ---------------------------- #

# >>> Binary <<<
# Time Complexity: O(log n) 
# Space Complexity: O(1)
# Notes:
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """

        s, e, res = 0, x, 0

        while s <= e:
            m = (s + e) // 2
            if m*m == x:
                return m
            elif m*m > x: #search left
                e = m - 1
            elif m*m < x: #search right
                s = m + 1
                res = m # Highest midpoint we've seen so far that satisfies condition.
        return res

# ---------------------------- #

# >>> Brute Force <<<
# Time Complexity: O(n^ 1/2) / O(sqrt(N))
# Space Complexity: O(1)
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