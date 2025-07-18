# LeetCode link: https://leetcode.com/problems/counting-bits/description/
# Difficulty: Easy
# Notes: WATCH NEET

# ---------------------------- #

# >>> : <<<
# Time Complexity: 
# Space Complexity:
# Notes:
class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res = []

        for i in range(n+1):
            count = 0
            N = i
            while(N > 0):
                if N & 1 == 1:
                    count += 1
                N = N >> 1 # Same as dividing by 2

            res.append(count)
        
        return res
        

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