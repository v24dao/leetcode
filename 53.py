# LeetCode link: 
# Difficulty:
# Notes: Sliding window, greedy, dp?

# ---------------------------- #

# >>> Kadane's Algorithm (Sliding Window) <<<
# Time Complexity: O(n)
# Space Complexity: O(1)
# Notes:

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ## Kadane's Algorithm!
        L,maxL,maxR = 0,0,0
        curr_sum, max_sum = 0, nums[0]

        for R in range(len(nums)):
            
            # If the sum of the current subarray (before R) is negative,
            # this subarray is not contributing positively to achieving a larger sum.
            # We can disregard it.
            if curr_sum < 0:
                curr_sum = 0
                L = R
            
            curr_sum += nums[R]
            if curr_sum > max_sum:
                max_sum = curr_sum
                maxL, maxR = L,R
        
        return max_sum
            

        
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