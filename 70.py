# LeetCode link: https://leetcode.com/problems/climbing-stairs/
# Difficulty:
# Notes: 

# ---------------------------- #

# >>> 'Naive' Recursion <<<
# Time Complexity: O(2^n)
# Space Complexity: 0(n)
# Notes: Doesn't work for as n grows (times out on LeetCode) -> Refer to LeetCode 509


# ---------------------------- #

# >>> Memoization implemented wrong <<<
# Time Complexity:
# Space Complexity: 
# Notes: Times out! -> hashmap does NOT persist!
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        hash = {0:1, 1:1}

        if n in hash:
            return hash[n]
        
        ret = self.climbStairs(n-2) + self.climbStairs(n-1)
        hash[n] = ret
        return ret

# ---------------------------- #

# >>> Top-down Dynamic Programming <<<
# Time Complexity: O(n) -> each value of k from 2 to n is only computed once, then it is stored.
# Space Complexity: O(n) -> each value of k from 0 to n is stored once in the memo dictionary (permanently). Values in the call stack (temporarily stored) reach a max depth of n (worst case scenario)
# Notes:
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        hash = {0:1, 1:1}
        def dp(k):
            if k not in hash:
                hash[k] = dp(k-2) + dp(k-1)
            return hash[k]
        return dp(n)

# ---------------------------- #

# >>> : <<<
# Time Complexity:
# Space Complexity: 
# Notes: