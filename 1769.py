# LeetCode link: https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box/description/?envType=problem-list-v2&envId=array
# Difficulty: Medium
# Notes: Need to learn a more elegant solution

# ---------------------------- #

# >>> Brute Force <<<
    # TC: O(n^2) => O(i*j) => typical nested loop. n == number of boxes
    # SC: O(1) according to leetcode editorial, since 'answer' is part of the output defined by the problem.
    # In reality, SC == 0(n), where n == number of boxes
    # Notes:
class Solution(object):
    def minOperations(self, boxes):
        """
        :type boxes: str
        :rtype: List[int]
        """
        ans = []
        for i in range(len(boxes)):
            operations = 0
            for j, val in enumerate(boxes):
                if val == '1':
                    # abs(i-j) = number of moves it takes to move ball from box j to box i.
                    operations += abs(i-j)
            ans.append(operations)
        return ans


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