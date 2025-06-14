# LeetCode link:
# Difficulty:
# Notes: 

# ---------------------------- #

# >>> Built in func + 2 pointers <<<
# Time Complexity: O(n)
# Space Complexity: O(n)
# Notes:
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s_list = list("".join(char for char in s if char.isalnum()).lower())
        #1 pointer at s_list[0]
        #1 pointer at s_list[n]
        n = len(s_list)
        for i in range(n/2):
            if s_list[i] != s_list[n-1-i]:
                return False
        return True

# ---------------------------- #

# >>> My O(1) Space Two Pointer  <<<
# Time Complexity: O(n)
# Space Complexity: O(1)
# Notes:
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def isAlphanumerical(c):
            return (ord("A") <= ord(c) <= ord("Z")) or (ord("a") <= ord(c) <= ord("z")) or ord('0') <= ord(c) <= ord('9')

        l,r = 0, len(s) - 1

        while l < r: 
            while not isAlphanumerical(s[l]) and l < len(s) - 1:
                l += 1
            while not isAlphanumerical(s[r]) and r >= 0:
                r -= 1
            if s[l].lower() != s[r].lower():
                return False 
            l, r = l + 1, r - 1
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