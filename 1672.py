# LeetCode link:
# Difficulty:
# Notes: All solutions have the same time and space complexity



# ---------------------------- #

# >>> 1st Attempt <<<
# Time Complexity: O(n^2) / O(n*m)
# Space Complexity: O(1)
# Notes:
class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        max = 0
        for i in range(len(accounts)):
            wealth = 0
            for j in range(len(accounts[i])):
                wealth += accounts[i][j]
            if wealth > max:
                max = wealth
        return max

# ---------------------------- #

# >>> More Pythonic <<<
# Time Complexity: 
# Space Complexity:
# Notes: 
# 1. Avoid names like 'max', since it is a built-in function in python.
# 2. Use sum() built-in function
# 3. Use max() built-in function
class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        max_wealth = 0
        for i in range(len(accounts)):
            wealth = sum(accounts[i])
            max_wealth = max(wealth, max_wealth)            
        return max_wealth
        
# ---------------------------- #

# >>> Even More Pythonic <<<
# Time Complexity:
# Space Complexity: 
# Notes: Loop directly over the customers in 'accounts', instead of using indexs
class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        max_wealth = 0
        for customer in accounts:
            wealth = sum(customer)
            max_wealth = max(wealth, max_wealth)        
        return max_wealth


# ---------------------------- #

# >>> One liner <<<
# Time Complexity:
# Space Complexity: 
# Notes:

class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        return max(sum(customer) for customer in accounts)
        