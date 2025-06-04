# LeetCode link: https://leetcode.com/problems/number-of-good-pairs/
# Difficulty: Easy
# Notes: 

# ---------------------------- #

# >>> Brute Force <<<
# Time Complexity: O(n^2) -> Nested loop
# Space Complexity: O(1) -> one integer variable!
# Notes:
class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        good_pairs = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] == nums[j] and i < j:
                    good_pairs += 1
        return good_pairs



# ---------------------------- #

# >>> Hashmap Solution <<<
# Time Complexity: O(n)
# Space Complexity: O(n)
# Notes: Solution relies on knowing n * n-1 // 2 -> n choose 2!!! -> binomial coefficient
# T/C explanation:
# two loops O(n) where n == number of variables in nums, and O(k) where k == number of unique variables in count. => O(n + k) => O(n) in this case
# S/C explanation:
# count stores the number of unique elements. In the worst case scenario, all elements are unique => O(n)
class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = {}
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        
        res = 0
        for num in count:
            res += count[num] * (count[num] - 1) // 2
        # n * (n-1) // 2

        return res

# ---------------------------- #

# >>> Pythonic Solution <<<
# Time Complexity: O(n)
# Space Complexity: O(n)
# Notes:

from collections import Counter
class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = Counter(nums)
        return sum( v * (v - 1) // 2 for v in count.values())
# ---------------------------- #

# >>> : <<<
# Time Complexity:
# Space Complexity: 
# Notes: