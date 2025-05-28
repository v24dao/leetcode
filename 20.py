# LeetCode link: https://leetcode.com/problems/valid-parentheses/
# Difficulty: Easy
# Notes: Good introduction to HashMaps and 'Pythonic code'

# ---------------------------- #

# >>> Non-pythonic solution <<<
# Time Complexity: 
# Space Complexity:
# Notes:
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hashMap = {')': '(', '}': '{', ']': '['}
        for i in range(len(s)):
            # Append opening brackets to our HashMap:
            if s[i] not in hashMap:
                stack.append(s[i])
            # Dealing with closing brackets:
            else:
                # Empty stack: Can't start with closing bracket!
                if len(stack) == 0:
                    return False
                # Closing bracket does not match with value at the top of stack:
                if stack[len(stack)-1] != hashMap[s[i]]:
                    return False
                # Closing bracket matches with value at the top of stack:
                stack.pop()
        # Empty stack means that all brackets match!
        if len(stack) == 0:
            return True
        return False 
# ---------------------------- #

# >>> Neet Solution with explanations <<<
# Time Complexity: O(n)
# Space Complexity: O(n)
# Notes:
# This solution is a lot more 'Pythonic'!
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {']': '[', '}':'{', ')':'('}
        for bracket in s:
            # Closing brackets:
            if bracket in closeToOpen: 
                # If stack is not empty, and brackets match:
                if stack and stack[-1] == closeToOpen[bracket]:
                    stack.pop()
                else:
                    return False
            # Opening brackets:    
            else:
                stack.append(bracket)
        
        return False if stack else True
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