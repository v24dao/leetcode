# LeetCode link: https://leetcode.com/problems/transform-array-by-parity/?envType=problem-list-v2&envId=array
# Difficulty: Easy
# Notes: Sometimes you just need to see the ball go in!

# ---------------------------- #

# >>> My Solution <<<
# Time Complexity: O(n)
# Space Complexity: O(1)
# Notes:
class Solution(object):
    def transformArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i, num in enumerate(nums):
            if num % 2 != 0:
                nums[i] = 1       # ✅ This works -> 'nums[i]' acceses the actual list
                # num = 1         # ❌ This does NOT work -> 'num' is simply a copy of nums at index i.
            else: 
                nums[i] = 0

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