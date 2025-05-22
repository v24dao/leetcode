# LeetCode link: https://leetcode.com/problems/add-digits/
# Difficulty: Easy
# Notes: 
# Not in NeetCode list. 
# Useful in Algo Trading apparently. Read comments/ watch YouTube videos for more efficient solution.

# ---------------------------- #

# >>> My Solution: 22/05/2025   <<<
# Time Complexity: O(log₁₀(n)) × d)
# Space Complexity: O(log₁₀(n))
# Notes: Do I need to understand TC/SC of this one on a deep level?

class Solution:
    def addDigits(self, num: int) -> int:
        while len(str(num)) > 1:
            temp = 0
            for i in range(len(str(num))):
                temp += int(str(num)[i])
            num = temp
        return num

# ---------------------------- #

# >>> Math Solution <<<
# Time Complexity: O(1)
# Space Complexity: 0(1)
# Notes: Based on modulo arithmatic and how numbers are represented in base 10.
class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0
        return 1 + (num - 1) % 9
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