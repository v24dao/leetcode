# LeetCode link: https://leetcode.com/problems/design-browser-history/description/
# Difficulty: Medium
# Notes: 
# Question can be solved with methods other than Doubly linked lists.
# Solve it with the other methods

# ---------------------------- #

# >>>  <<<
# Time Complexity: init => O(1), VISIT => O(1), BACK => O(n), FORWARD => O(n)
# Space Complexity: O(n) overall where n is the number of pages visited, O(1) for the individual operations
# Notes:

class ListNode:
    def __init__(self, val, prev = None, next = None):
        self.val = val
        self.prev = prev
        self.next = next
    
class BrowserHistory(object):

    def __init__(self, homepage):
        """
        :type homepage: str
        """
        self.current = ListNode(homepage)

    def visit(self, url):
        """
        :type url: str
        :rtype: None
        """
        # new_node = ListNode(url)
        # self.current.next = new_node #Point old page forward to the new one
        # new_node.prev = self.current #Point new page back to the old one
        # self.current = new_node #Set the new page as current

        self.current.next = ListNode(url, self.current)
        self.current = self.current.next

    def back(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        while self.current.prev and steps > 0:
            self.current = self.current.prev
            steps -= 1
        return self.current.val
        
    def forward(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        while self.current.next and steps > 0:
            self.current = self.current.next
            steps -= 1
        return self.current.val
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)

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