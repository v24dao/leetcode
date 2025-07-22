# LeetCode link: 
# Difficulty:
# Notes: 

# ---------------------------- #

# >>> My binary solution <<<
# Time Complexity: O(log n)
# Space Complexity: O(1)
# Notes:

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l,r,first_bad = 1, n, n

        while l <= r: # Terminates when l and r cross.
            m = (l + r) // 2
            if isBadVersion(m): #Search left,
                first_bad = min(m, first_bad)
                r = m - 1 # r may be Good OR Bad in this version.
            else: #Search right
                l = m + 1
            
        return first_bad


# ---------------------------- #

# >>> Gregg Hogg <<<
# Time Complexity: O(log n)
# Space Complexity: O(1)
# Notes: https://www.youtube.com/watch?v=vnfGi-ucwTE&ab_channel=GregHogg

# This is a 'less' intuitive but cleaner version (Gregg Hog):
    # We set the while loop to be l < r, so it terminates when l == m == r.
    # We would also set r = m 
    # This means that we ALWAYS keep the leftmost/earliest 'bad' value
    # We can then return the last L/R (they are the same anyways)

# Pretty intuitive when coded out:
class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """

        L, R = 0, n

        while L < R:
            M = (L + R)// 2
            if isBadVersion(M): # Search left to find a bad version that comes earlier
                R = M
            else: # Search right to find a bad version
                L = M + 1
        
        # Terminates when L == R == leftmost bad version
        return L

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