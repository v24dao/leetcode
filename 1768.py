# LeetCode link: https://leetcode.com/problems/merge-strings-alternately/description/
# Difficulty: Easy
# Notes: 
    # Strings are iterable!
    # We can do string1[0], string1[1], etc
    # Read notes on differences between .append() and .extend() for this question

# ---------------------------- #

# >>> OG solution <<<
# Time Complexity: O(n^2 + m^2)
    # n = length of list 1. 0(n) to pop from list 1. O(n^2) to pop all from list 1.  
# Space Complexity: O(n + m)
# Notes:
class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        word1, word2 = list(word1), list(word2)
        merged = []
        while word1 and word2:
            merged.append(word1.pop(0))
            merged.append(word2.pop(0))
        if word1 and not word2:
            merged.extend(word1)
        else:
            merged.extend(word2)
        res = "".join(merged)
        return res

# ---------------------------- #

# >>> NEET <<<
# Time Complexity:
# Space Complexity: 
# Notes:
class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        #Appending and updating string (e.g. res) is NOT efficient. Strings are immutable, so updating a string will only create a new one.
        i, j = 0,0
        res = []
        while i < len(word1) and j < len(word2):
            res.append(word1[i])
            res.append(word2[j])
            i += 1
            j += 1
        # Using .extend() adds the rest of the word 1 character at a time.
        # This is better for maintaining consistency and code quality. Can be useful incase intermediate results matter. 
        # For our case, it does NOT matter.
        # .append(word1[i:]) adds the rest of word one as 1 string.
        res.append(word1[i:])
        res.append(word2[j:])
        return "".join(res)
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