# LeetCode link: https://leetcode.com/problems/find-words-containing-character/description/
# Difficulty: Easy
# Notes: Very easy tbh

# ---------------------------- #

# >>>  <<<
# TC: O(nxm) => where n = number of words, m = avg length of words
# SC: O(n), where n = number of words
# Notes:
class Solution(object):
    def findWordsContaining(self, words, x):
        """
        :type words: List[str]
        :type x: str
        :rtype: List[int]
        """
       
        ans = []
        for i, word in enumerate(words):
            if x in word:
                ans.append(i)
        return ans


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