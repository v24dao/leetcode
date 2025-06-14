# LeetCode link: https://leetcode.com/problems/largest-local-values-in-a-matrix
# Difficulty: Easy
# Notes: 

# ---------------------------- #

# >>> BRUTE FORCE <<<
# Time Complexity: 
# Space Complexity:
# Notes:
class Solution(object):
    def largestLocal(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[List[int]]
        """
        res = []
        n = len(grid)
        for i in range(0,n-2):
            current_row_results = []
            for j in range(0,n-2):
                max_in_3x3 = -float('inf')
                for x in range(i,i+3):
                    for y in range(j,j+3):
                        max_in_3x3 = max(max_in_3x3, grid[x][y])
                current_row_results.append(max_in_3x3)
            res.append(current_row_results)
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

# ---------------------------- #

# >>> : <<<
# Time Complexity:
# Space Complexity: 
# Notes: