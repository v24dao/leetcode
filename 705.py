# LeetCode link: https://leetcode.com/problems/design-hashset/
# Difficulty: Easy
# Notes: 
# https://www.youtube.com/watch?v=VymjPQUXjL8&ab_channel=NeetCodeIO
# Learn how to implement it properly after learning 

# ---------------------------- #

# >>> My solution (inefficient) <<<
# Time Complexity: Look below
# Space Complexity: O(1) for each operation
# Notes:
    # Linear search
    # Use of python list (dynamic array)
class MyHashSet(object):

    # O(1) time
    def __init__(self):
        self.hash = []  
    # O(n) time
    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        for i in range(len(self.hash)):
            if self.hash[i] == key:
                return
        self.hash.append(key)
    # O(n) time    
    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        for i in range(len(self.hash)):
            if self.hash[i] == key:
                self.hash.pop(i)
                return # This line stops it from looping!
                # 1. it is pointless to loop, since we have already found our value
                # 2. looping to len(self.hash) after a value has been removed will result in an out of bounds error!
    # O(n) time
    def contains(self, key):
        """
        :type key: int
        :rtype: bool
        """
        for i in range(len(self.hash)):
            if self.hash[i] == key:
                return True
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

# ---------------------------- #

# >>> : <<<
# Time Complexity:
# Space Complexity: 
# Notes: