# LeetCode link: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/
# Difficulty: Medium
# Notes: 
# 2 Pointer is optimal. 
# Brute force can be too slow/ time out. 
# Hashmap -> not O(n) space so doesn't count
# Binary search per i

# ---------------------------- #

# >>> 2 Pointer optimal <<<
# Time Complexity: O(n)
# Space Complexity: O(1)
# Notes:
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Take advantage of sorted array.
        # if res > target, we need res to be a smaller number, so decrement r.
        # if res < target, we need res to be a larger number, so increment l.
        l, r = 0, len(numbers) - 1
        while l < r:
            res = numbers[l] + numbers[r]
            if res == target:
                return [l+1,r+1]
            elif res < target:
                l+=1
            else: 
                r-=1

# ---------------------------- #

# >>> Binary search per i => works but inefficient <<<
# Time Complexity: O(nlogn)
# Space Complexity: O(1)
# Notes:
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        # i = first element
        # we do binary search from i+1 to end of array to try and find a match
        for i in range(len(numbers) - 1):
            desired_number = target - numbers[i]
            l, r = i + 1, len(numbers) - 1
            while l <= r:
                m = (l + r) / 2
                if desired_number == numbers[m]:
                    return [i+1, m+1]
                elif desired_number < numbers[m]: # Search left
                    r = m - 1
                else: # Search right
                    l = m + 1

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