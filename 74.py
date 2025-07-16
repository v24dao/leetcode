# LeetCode link: https://leetcode.com/problems/search-a-2d-matrix/
# Difficulty: Medium
# Notes: Code again, learn flatterned version

# ---------------------------- #

# >>> 2 binary searches <<<
# Time Complexity: O(log n + log m)
# Space Complexity:
# Notes:
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # Example:
        #  [ [0,0]
        #    [1,1]
        #    [2,2] ]
        # n = 2, m = 3

        COLS = len(matrix[0]) 
        ROWS = len(matrix)
        
        # Start with rows 
        top, bot = 0, ROWS - 1

        while top <= bot:
            row = (top + bot) // 2
            if target < matrix[row][0]:
                bot = row - 1
            elif target > matrix[row][COLS-1]:
                top = row + 1
            else:
                break
        
        #If row hasn't been found:
        if top > bot:
            return False

        row = (top + bot) // 2
        l,r = 0, COLS - 1
        while l <= r:
            m = (l + r) // 2
            if target == matrix[row][m]:
                return True
            elif target < matrix[row][m]:
                r = m - 1
            else:
                l = m + 1
        return False
        
        

# ---------------------------- #

# >>> Flatterned 2D matrix <<<
# Time Complexity:
# Space Complexity: 
# Notes:
#row = k // n
#col = k % n
#value = matrix[row][col]


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