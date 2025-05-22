# LeetCode link: https://leetcode.com/problems/remove-element/description/
# Difficulty: Easy
# Notes: 

# ---------------------------- #

# >>> My Two Pointer Solution: 22/05/2025 <<<
# Time Complexity: O(n)
# Space Complexity: O(1)
# Notes: 
# NeetCode has the same 2 pointer solution.
# 
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # left pointer: keeps track of non 'val' occurrences
        # right pointer: scans the array
        left = 0
        for right in range(len(nums)):
            if nums[right] != val:
                nums[left] = nums[right]
                left += 1
        return left


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