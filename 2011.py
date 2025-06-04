# LeetCode link: https://leetcode.com/problems/final-value-of-variable-after-performing-operations/
# Difficulty: Easy
# Notes: Look at more pythonic solution

# ---------------------------- #

# >>> First Solution <<<
# Time Complexity: O(n)
# Space Complexity:O(1)
# Notes:
class Solution(object):
    def finalValueAfterOperations(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        X = 0
        for operation in operations:
            if operation == "--X" or operation == "X--":
                X-= 1
            else: 
                X+= 1
        return X


# ---------------------------- #

# >>> More Pythonic Solution <<<
# Time Complexity: O(n)
# Space Complexity: O(1)
# Notes:
class Solution(object):
    def finalValueAfterOperations(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        X = 0
        for operation in operations:
            if '-' in operation:
                X-=1 
            else:
                X+=1
        return X


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