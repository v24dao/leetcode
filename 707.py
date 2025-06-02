# LeetCode link: https://leetcode.com/problems/design-linked-list/
# Difficulty: Medium
# Notes: Not on Neet150/250

# ---------------------------- #

# >>> My DLL solution <<<
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

# >>> My SLL Solution <<<
# Time Complexity: 
# Space Complexity: 
# Notes: I want to cry. Don't get tripped up by off 1 errors!

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList(object):

# [self.head] -> [10] -> [20] -> None
    #              ↑       ↑
    #    self.head.next   self.tail

    def __init__(self):
        self.head = ListNode(0)
        self.tail = self.head
        self.length = 0
        # self.head.next points to the first node
        # self.tail.next points to the last node

    def get(self, index):
        """
        :type index: int
        :rtype: int
        """
        if index < 0 or index >= self.length:
            return -1
        current = self.head.next
        i = 0 
        while current:
            if i == index:
                return current.val
            current = current.next
            i += 1
        
    def addAtHead(self, val):
        """
        :type val: int
        :rtype: None
        """
        new_node = ListNode(val)
        new_node.next = self.head.next # Point new node to the old head
        self.head.next = new_node # move head pointer to the new node
        if self.length == 0: # If list was previously empty
            self.tail = new_node
        self.length += 1

    def addAtTail(self, val):
        """
        :type val: int
        :rtype: None
        """
        new_node = ListNode(val)
        self.tail.next = new_node # Point the old tail to new node
        self.tail = new_node # Set the new node as the tail
        if self.length == 0: # If list was previously empty
            self.head.next = new_node
        self.length += 1 

    
    def addAtIndex(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        if index < 0 or index > self.length:
            return
        if index == 0:
            self.addAtHead(val)
            return
        if index == self.length:
            self.addAtTail(val)
            return

        new_node = ListNode(val)
        prev = self.head
        current = self.head.next
        i = 0
        while current:
            if i == index:
                prev.next = new_node
                new_node.next = current
                self.length += 1
                return
            prev = prev.next
            current = current.next
            i += 1
        # Edge cases, adding at head/tail
        # Index = 0 => add at head
        # Index = self.length => add at tail

        
    def deleteAtIndex(self, index):
        """
        :type index: int
        :rtype: None
        """
        if index < 0 or index >= self.length:
            return

        prev = self.head
        current = self.head.next
        i = 0
        while current:
            if i == index:
                prev.next = current.next # Soft delete
                if current == self.tail:
                    self.tail = prev
                self.length -= 1
                return
            prev = prev.next
            current = current.next
            i += 1
        # Edge cases, Removing at head/tail
        # Index = self.length - 1 => Move tail pointer

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