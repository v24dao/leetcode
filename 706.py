# LeetCode link: https://leetcode.com/problems/design-hashmap/
# Difficulty: Easy
# Notes: 
# Learn how to implement it properly after learning 

# ---------------------------- #

# >>> My solution (inefficient) <<<
# Time Complexity: 
# Space Complexity: 
# Notes:
    # Linear search
    # Use of python list (dynamic array)
class MyHashMap(object):
    # O(1) TC
    def __init__(self):
        self.keys = []
        self.values = []
    # O(n) TC
    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        for i in range(len(self.keys)):
            if self.keys[i] == key:
                self.values[i] = value
                return 
        else:
            self.keys.append(key)
            self.values.append(value)
    # O(n) TC
    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        for i in range(len(self.keys)):
            if self.keys[i] == key:
                return self.values[i] 
        return -1
    # O(n) TC
    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        for i in range(len(self.keys)):
            if self.keys[i] == key:
                self.keys.pop(i)
                self.values.pop(i)
                return

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