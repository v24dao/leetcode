# LeetCode link: https://leetcode.com/problems/min-stack/
# Difficulty: Medium
# Notes: Needed 

# ---------------------------- #

# >>> My Solution: 30/05/2025 <<<
# Time Complexity: O(1) -> time complexity for each function
# Space Complexity: O(n) -> overall space complexity 
# Notes: Look into pep8! -> Python industry standard is not camelCase
# https://realpython.com/python-pep8/#:~:text=PEP%208%2C%20sometimes%20spelled%20PEP8,enhancing%20code%20readability%20and%20consistency.

class MinStack:

    def __init__(self):
       self.stack = [] #Regular stack
       self.minStack = [] #Keeps track of the min value as we add to our other stack

    def push(self, val: int) -> None:
        # Add value to normal stack
        self.stack.append(val)
        # Add value to min stack if: a) min stack is empty. b) val is smaller than top of min stack.
        if not self.minStack or val < self.minStack[-1]:
            self.minStack.append(val)
        else:
            self.minStack.append(self.minStack[-1])
        
    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
        
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