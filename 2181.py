# LeetCode link: https://leetcode.com/problems/merge-nodes-in-between-zeros/
# Difficulty: Medium
# Notes: 

# ---------------------------- #

# >>> My Solution - In place <<<
# Time Complexity: O(n)
# Space Complexity: O(1)
# Notes: 
# (*) Edge case of 'right.next == None' is totally avoided
    # This is because we set left.next equal to right.next
    # Therefore, when right.next == None, left.next == None too

class Solution(object):
    def mergeNodes(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # 2 Pointer:
        # lp: keeps track of the last node in the list we are keeping
        # rp: iterates through the original node list

        left, right = head, head
        while right:
            if right.val == 0: # *
                left.next = right.next
                left = left.next
            #Edge case: 
                #right.val != 0 AND left == right
                #We don't want the value at this edge case to count twice!
            elif left != right: 
                left.val += right.val
            right = right.next
        return head.next


# ---------------------------- #

# >>> Neet - New List <<<
# Time Complexity: O(n) where n is length of original LL
# Space Complexity: O(k) where k is the number of segments
# Notes:
class Solution(object):
    def mergeNodes(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        current = head
        dummy = ListNode(0)
        tail = dummy

        while current.next:
            if current.val == 0:
                tail.next = ListNode(0)
                tail = tail.next
            else:
                tail.val += current.val
            current = current.next

        return dummy.next

# ---------------------------- #

# >>> Neet: in-place <<<
# Time Complexity: O(n)
# Space Complexity: O(1)
# Notes:
class Solution(object):
    def mergeNodes(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # 2 pointer:
            # left pointer -> keeps track of the last node in list we are returning
            # right pointer -> iterates through the nodes
        
        cur = head
        while cur.next:
            node, cur = cur.next, cur.next #Points 1st non-zero value after 0 
            while cur.next.val != 0:
                node.val += cur.next.val
                cur = cur.next
            #Code below executes ONLY when cur.next.val == 0
            cur = cur.next #Points to 0
            node.next = cur.next #Points to 1st non-zero value after 0
        return head.next
# ---------------------------- #

# >>> : <<<
# Time Complexity:
# Space Complexity: 
# Notes: