# Solution link: https://leetcode.com/problems/remove-duplicates-from-sorted-array/
# Difficulty: Easy
# Notes: 
 
# ---------------------------- #

# >>> 2 Pointer Solution: 21/05/2025 <<<
# Time Complexity: O(n) 
# Space Complexity: O(1)
# Notes: 
# TC is O(n), because you iterate list once. This means that TC depends on length of the list.
# SC is O(1), because solution is in place. No extra memory needed.

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Non-decreasing order means that the next number is always equal or greater.
        # We want two pointers:
        # 1st (left) counter: next available index / number of unique values 
        # 2nd (right) counter: the element we are currently comparing 

        k,c = 1,1
        for c in range(1,len(nums)):
            if nums[c] != nums[k-1]:
                nums[k] = nums[c]
                k += 1
        return k

# ---------------------------- #

# >>> Neet: 2 Pointer Solution <<<
# Time Complexity: O(n)
# Space Complexity: O(1) 
# Notes:
# Very similary to my solution!
# I declared the right pointer twice, which is redundant. 
# I compare the right pointer to the last unique number that was indentified. 
# This works but is NOT neccesary, because the list is sorted! Just compare the right pointer to the value that came before it, instead.

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 1

        for r in range(1,len(nums)):
            if nums[r] != nums[r - 1]:
                nums[l] = nums[r]
                l += 1
        return l