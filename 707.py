# LeetCode link: https://leetcode.com/problems/design-linked-list/
# Difficulty: Medium
# Notes: Not on Neet150/250

# ---------------------------- #

# >>> : <<<
# Time Complexity: get => O(n), addAtHead => O(1), addAtTail => O(1), addAtIndex => O(n), deleteAtIndex => O(n)
# Space Complexity: O(n) -> n = number of elements/nodes
# Notes:
class ListNode:
    def __init__(self,val):
        self.val = val
        self.prev = None
        self.next = None

class MyLinkedList(object):
    def __init__(self):
        # These are dummy nodes! -> Helps us to avoid edge cases
        self.left = ListNode(0)
        self.right = ListNode(0)
        self.left.next = self.right
        self.right.prev = self.left
        
    def get(self, index):
        """
        :type index: int
        :rtype: int
        """
        current = self.left.next
        i = 0
        while current and current != self.right and index >= 0:
            if i == index:
                return current.val
            current = current.next
            i += 1
        return -1
        

    def addAtHead(self, val):
        """
        :type val: int
        :rtype: None
        """
        new_node, Next, Prev = ListNode(val), self.left.next, self.left
        Prev.next = new_node
        Next.prev = new_node
        new_node.prev = Prev
        new_node.next = Next
        

    def addAtTail(self, val):
        """
        :type val: int
        :rtype: None
        """
        new_node, Next, Prev = ListNode(val), self.right, self.right.prev
        Prev.next = new_node
        Next.prev = new_node
        new_node.prev = Prev
        new_node.next = Next

    def addAtIndex(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        current = self.left.next
        i = 0
        while current and current != self.right.next and index >= 0:
            if i == index:
                new_node, Next, Prev = ListNode(val), current, current.prev 
                # Next = current => This is because we are inserting before current!
                Prev.next = new_node
                Next.prev = new_node
                new_node.prev = Prev
                new_node.next = Next
                return 
            current = current.next
            i += 1

    def deleteAtIndex(self, index):
        """
        :type index: int
        :rtype: None
        """
        # Edge case: Do not try to delete dummy node or any nodes that are out of bounds.
        current = self.left.next
        i = 0
        while current and current != self.right and index >= 0:
            if index == i:
                Prev, Next = current.prev, current.next
                # 'Soft-delete'
                Prev.next = Next
                Next.prev = Prev
                return
            current = current.next
            i += 1

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