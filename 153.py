# LeetCode link:
# Difficulty: Medium
# Notes: Brute force, binary

# ---------------------------- #

# >>> Brute force <<<
# Time Complexity: O(n)
# Space Complexity: O(1)
# Notes:

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # Edge case 1: Only 1 value
        if len(nums) == 1:
            return nums[0]

        # Edge case 2: Not rotated at all
        if nums[0] < nums[len(nums) - 1]:
            return nums[0]
    
        # Brute Force
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                return nums[i]

# ---------------------------- #

# >>> Neet - Binary Search <<<
# Time Complexity: O(logn)
# Space Complexity: O(1)
# Notes: 
    # Bit different from classic binary search.
    # If sub-array is sorted, nums[l] is potentially the lowest value. We can assume that the rest of the sub-array is greater than nums[l].
    # We need to compare nums[m] with lowest for every m calculated. This is because this solution excludes m when searching left or right.
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l,r = 0, len(nums) - 1
        lowest = 5001

        while l <= r:
            # Edge case: Rest of the array is sorted / There is 1 value left
            if nums[l] <= nums[r]:
                lowest = min(nums[l], lowest)
                break
            
            # Perform binary search:
            m = (l + r) // 2
            lowest = min(lowest, nums[m])

            if nums[m] > nums[r]: # search right, since point of infliction is between index m and r (inclusively).
                l = m + 1
            else: # search left.
                r = m - 1

        return lowest

# ---------------------------- #

# >>> My approach <<<
# Time Complexity:
# Space Complexity: 
# Notes:
# Edge cases explained: 
    # 1. Our sub-array is sorted in ascending order, meaning that the lowest value is the first value (nums[l])
    # 2. There is only 1 value left (l == m == r), so this value must be the lowest.
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l,r = 0, len(nums) - 1

        while l <= r:
            # Edge cases: 
            # 1. Rest of the array is sorted
            # 2. There is only 1 value left 
            if nums[l] <= nums[r]:
                return nums[l]
            
            # Perform binary search:
            m = (l + r) // 2

            if nums[m] > nums[r]: # min is to the right
                l = m + 1
            else: # min is at m or to the left
                r = m 
# ---------------------------- #

# >>> : <<<
# Time Complexity:
# Space Complexity: 
# Notes: