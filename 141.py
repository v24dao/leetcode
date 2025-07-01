# LeetCode link:https://leetcode.com/problems/linked-list-cycle/description/
# Difficulty:Easy
# Notes: 
    # Two pointers method:
    # Fast and slow. Floyd's tortoise and Hare algo.
    # If there is no cycle, fast is never equal to slow. 
    # Hashset method:
    # If you visit a node that is already in the hashset, you have a cycle!
    # If it's your first time visiting a node, add it to your hashset. 
    
# ---------------------------- #

# >>> 2 Pointer <<<
# Time Complexity: O(n)
# Space Complexity: O(1)
# Notes:

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        fast = head
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False
# ---------------------------- #

# >>> Hashset <<<
# Time Complexity: O(n)
# Space Complexity: O(n)
# Notes:
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        visited = set()
        while head:
            if head in visited:
                return True
            else: 
                visited.add(head)
                head = head.next
        return False
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