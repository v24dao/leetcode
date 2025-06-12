# LeetCode link:
# Difficulty: Easy
# Notes: Very easy tbh. Just focus on making code 'Pythonic'

# ---------------------------- #

# >>> My solution <<<
# Time Complexity: 
# Space Complexity:
# Notes:
class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        res = []
        max_candies = max(candies)
        for candie in candies:
            if candie + extraCandies >= max_candies:
                res.append(True)
            else:
                res.append(False) 
        return res

# ---------------------------- #

# >>> More Pythonic code <<<
# Time Complexity:
# Space Complexity: 
# Notes:
class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        max_candies = max(candies)
        return [candie + extraCandies >= max_candies for candie in candies]
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