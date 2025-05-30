# LeetCode link: https://leetcode.com/problems/merge-two-sorted-lists/
# Difficulty: Easy
# Notes: 

# ---------------------------- #

# >>> Completed with hints from GFG <<<
# Time Complexity: O(n + m) where n and m are length of the LL's respectively
# Space Complexity: O(1)
# Notes: 
# Needed hints -> Use a dummy, and 'current' counter 

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(-1)
        current = dummy

        while list1 is not None and list2 is not None:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else: 
                current.next = list2
                list2 = list2.next
            # Don't forget to move the current pointer!!!!
            current = current.next 
        
        while list1 is not None:
            current.next = list1
            list1 = list1.next
            current = current.next
        
        while list2 is not None:
            current.next = list2
            list2 = list2.next
            current = current.next
        
        return dummy.next


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