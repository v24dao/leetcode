# LeetCode link: https://leetcode.com/problems/sort-colors/
# Difficulty: Medium
# Notes: 
    # Bucket sort is probably the best approach
    # 2 pass bucket sort beats 100% T/C in python

# ---------------------------- #

# >>> Bucket sort <<<
# Time Complexity: O(n)
# Space Complexity: O(1)
# Notes:
    # First for loop is O(n) T/C
    # 2nd for loop is O(n) T/C
    # O(2n) evaluates to O(n)

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = [0,0,0]

        for i in range(len(nums)):
            count[nums[i]] += 1

        j = 0

        for i in range(len(nums)):
            while count[j] == 0:
                j+= 1
            nums[i] = j
            count[j] -= 1

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