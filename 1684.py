# LeetCode link:
# Difficulty:
# Notes: 

# ---------------------------- #

# >>> Brute Force <<<
# Time Complexity: O(n*m) -> number of words * length of words 
# Space Complexity: O(n)
# Notes:
class Solution(object):
    def countConsistentStrings(self, allowed, words):
        """
        :type allowed: str
        :type words: List[str]
        :rtype: int
        """
        allowed_letters = list(allowed)
        res = len(words)
        for word in words:
            for letter in word:
                if letter not in allowed_letters:
                    res -= 1
                    break #Breaks out of the inner for loop
        return res
                
        

# ---------------------------- #

# >>> GPT <<<
# Time Complexity:
# Space Complexity: 
# Notes: More pythonic (idiomatic) and performant.
class Solution(object):
    def countConsistentStrings(self, allowed, words):
        """
        :type allowed: str
        :type words: List[str]
        :rtype: int
        """
        allowed_set = set(allowed)
        res = 0
        for word in words:
            if all(letter in allowed_set for letter in word):
                res += 1
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