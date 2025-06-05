# LeetCode link:
# Difficulty: Easy
# Notes: Couldn't solve by myself. 

# ---------------------------- #

# >>> NeetCode: 2 Pointer <<<
# Time Complexity: O(n) -> Since we are iterating through the linked list
# Space Complexity: O(1) -> We're just using pointers. No Data Structures
# Notes:

class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # T/C: 0(n) 
        # S/C: 0(1) 
        ## 2 Pointer Method: 
        prev = None #Keeps track of the previous value
        current = head #Keeps track of the current value

        while current: # While current != None 
            temp_next = current.next # Temporarily holds the next node 
            current.next = prev # Point to the left
            # We are now ready to Move onto the next node:
            prev = current # Move prev counter to the right
            current = temp_next # Also move current pointer to the right
        
        # Once we reach the end of the linked list:
        # prev will point to the last Node in the original LL.
        # Current will point to None
    
        return prev # This returns the tail Node of the original LL (which is the head of new LL)


        

# ---------------------------- #

# >>> NeetCode Recursion <<<
# Time Complexity: O(n)
# Space Complexity: O(1)
# Notes: Worse than the 2 Pointer solution but still worth knowing
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # Edge Case:
        if not head:
            return None
        # Base Case:
        # This is what gets returned if we ARE at the end of the original linked list.
        # new_head variable gets overwritten if we are NOT at the end of the original linked list.
        new_head = head 

        # Recursive case:
        if head.next:
            #This is what gets returned if we are NOT at the end of the original linked list.
            new_head = self.reverseList(head.next) 
            head.next.next = head # point the next node back to current node
        head.next = None # Point current head to None
        return new_head

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