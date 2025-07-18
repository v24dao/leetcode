# LeetCode link: https://leetcode.com/problems/number-of-1-bits/
# Difficulty: Easy 
# Notes: 32 bit integer => O(32) => O(1) or constant time!
# Can easily be mistaken for O(log n).
# Max iterations is 32 (a constant). No dependency on the magnitude of n. 

# ---------------------------- #

# >>> : <<<
# Time Complexity: O(32) -> O(1)
# Space Complexity: O(1)
# Notes:

class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0

        while(n > 0):
            if n & 1 == 1:
                count += 1
            n = n >> 1 #Same as n // 2
        
        return count

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