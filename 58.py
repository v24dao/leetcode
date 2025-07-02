# LeetCode link:
# Difficulty:
# Notes: 

# ---------------------------- #

# >>> My solution <<<
# Time Complexity: O(n) 
# Space Complexity: O(1)
# Notes:
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        count, i = 0, len(s) - 1
        # We start at the end of the string
        # Iterate until we find the end of the last word.
        while i >= 0:
            if s[i].isalpha():
                break
            i -= 1
        # Iterate until we find a non-alpha character. 
        # We now have the length of our last word.
        while i >= 0 and s[i].isalpha():
            count += 1
            i -= 1
        return count


# ---------------------------- #

# >>> Neet <<<
# Time Complexity: O(n)
# Space Complexity: O(1)
# Notes: 
# Same as mine, but more pythonic.
# More efficient to check for empty space " " than it is to check for alpha char.

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        i, count = len(s) - 1, 0

        while s[i] == " ":
            i -= 1
        while i >= 0 and s[i] != " ":
            count += 1
            i -= 1
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