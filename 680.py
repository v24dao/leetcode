# LeetCode link:
# Difficulty:
# Notes: 

# ---------------------------- #

# >>> Neet <<<
# Time Complexity: O(n)
# Space Complexity: O(1)
# Notes:
# 2 Pointer problem:
        # l pointer starts at 0
        # r pointer starts at len(s) - 1
        # whilst l < r
        # if s[l] == s[r], l += 1, r -= 1
        # if s[l] != s[r]:
            # we can skip a character on the left or right, then check whether the remainder is a palindrome
class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l, r = 0, len(s) - 1

        while l < r:
            if s[l] != s[r]:
                skipL, skipR = s[l+1:r+1], s[l:r]
                return skipL == skipL[::-1] or skipR == skipR[::-1]
            l += 1
            r -= 1
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