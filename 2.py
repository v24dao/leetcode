# LeetCode link:
# Difficulty:
# Notes: Linked lists

# ---------------------------- #

# >>> My Solution <<<
# Time Complexity: O(n + m)
# Space Complexity: O(n + m)
# Notes:

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
        carry = 0
        dummy = ListNode(0)
        curr = dummy

        while l1 or l2:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0

            # Update new digit:
            val = (l1_val + l2_val + carry) % 10
            carry = (l1_val + l2_val + carry) // 10
            curr.next = ListNode(val)

            # Update pointers:
            curr = curr.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        # Edge case: Carry left over
        if carry:
            curr.next = ListNode(carry)

        return dummy.next

# ---------------------------- #

# >>> Navdeep Singh <<<
# Time Complexity: O(n + m)
# Space Complexity: O(n + m)
# Notes: Deals with the edge case where l1== 0 l2==0 and carry != 0 more elegantly.

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
        carry = 0
        dummy = ListNode(0)
        curr = dummy

        while l1 or l2 or carry:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0

            # Update new digit:
            val = (l1_val + l2_val + carry) % 10
            carry = (l1_val + l2_val + carry) // 10
            curr.next = ListNode(val)

            # Update pointers:
            curr = curr.next
            l1 = l1.next if l1 else 0
            l2 = l2.next if l2 else 0

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