# LeetCode link:
# Difficulty:
# Notes: 

# ---------------------------- #

# >>> Neet <<<
# Time Complexity:
# Space Complexity: 
# Notes:

#Sort from right to left. Bigger values on the right.

# last = the index we are copying values to.
# m = number of vals left to sort from original nums1.
# n = number of vals left to sort from nums2.

# if m == 0, but n > 0:
    # We need to put the remainder of nums2 into nums1.
# if m > 0, but n == 0:
    # No values left in nums2.
    # The rest of nums1 is already sorted, so no need to do anything.


class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        # Start merging at the end of nums1
        # m = number of values left to sort from original nums1.
        # n = number of values left to sort from nums2.
        # If we have 1 more value to sort in nums2: n = 1, index = 0 (n-1)
        last = m + n - 1

        while m > 0 and n > 0:
            if nums2[n-1] > nums1[m-1]:
                nums1[last] = nums2[n-1]
                n -= 1
            else: 
                nums1[last] = nums1[m-1]
                m -= 1
            last -= 1
        # Once we've sorted all the original values in nums1, we fill nums1 with the remainder of nums2.
        # If the first while loop ends because we've run out of values in nums2... do nothing.
        # => the rest of nums1 is already sorted! 
        while n > 0:
            nums1[last] = nums2[n-1]
            last -= 1
            n -= 1

# ---------------------------- #
# >>> Ineffective <<<
# Time Complexity:
# Space Complexity: 
# Notes:
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        for i in range(n):
            nums1[m+i] = nums2[i]
        
        for i in range(m+n):
            j = i
            #nums1[j-1] nums1[j]
            while j >= 1 and nums1[j] < nums1[j-1]:
                nums1[j-1], nums1[j] = nums1[j], nums1[j-1]
                j -= 1
# ---------------------------- #



# >>> FIX <<<
# Time Complexity: 
# Space Complexity:
# Notes:
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        p1, p2 = 0, 0

        while p1 < m + n and p2 < n:
            if nums1[p1] == 0:
                nums1[p1] = nums2[p2]
                p1 += 1
                p2 += 1
            if nums1[p1] <= nums2[p2]:
                p1 += 1
            else:
                x = m + n - 2
                while x >= p1:
                    nums1[x+1] = nums1[x]
                    x -= 1
                nums1[p1] = nums2[p2]
                p1 += 1
                p2 += 1
        # Would it be cheating to replace all the zeros with nums2, then just use a normal sorting algo?
        # 2 pointer:  
        # Scenario 1:
            #nums1[p1] == 0
            #nums1[p1] = nums2[p2]
            # increment p1 and p2  
        # Scenario 2:
            # nums1[p1] <= nums2[p2] 
            # increment p1
        # Scenario 3:
            # nums2[p2] < nums1[p1]
            # Move all values in nums1 over to the right (from p1 to the 2nd last element)
            # Set nums1[p1] = nums2[p2]
            # increment p2 
            # increment p1 
        
        # [1,2,3,0,0,0]
        # [2,5,6]

        # p1 = 0, p2 = 0
        # value at p1 <= value at p2
        # p1 = 1, p2 = 0
        # value at p1 <= value at p2
        # p1 = 2, p2 = 0
        # value at p2 < value at p1
        # move all values 1 over in the p1 array
        # start at x = (m + n - 2 ), while x >= p1: nums1[x+1] = nums1[x]. decrement x.
        # [1,2,0,3,0,0]
        # nums1[2] = nums2[0]
        # [1,2,2,3,0,0]
        # p1 = 3, p2 = 1
        # value at p1 <= value at p2
        # p1 = 4, p2 = 1
        # value at p1 is 0:
        # nums1[p1] = nums2[p2]
        # [1,2,2,3,5,0]
        # p1 = 5, p2 = 2. value at p1 == 0
        # nums1[5] = nums2[2]
        # p1 += 1, p2 += 1 => p1 = 6, p2= 3 => out of bound, end.

        ## DOES NOT WORK for cases where there are 0s throughout!

#failed test case:
# nums1 = [-1,0,0,3,3,3,0,0,0]
# m = 6
# nums2 = [1,2,2]
# n = 3
# ---------------------------- #

# >>> : <<<
# Time Complexity:
# Space Complexity: 
# Notes: