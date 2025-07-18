# LeetCode link: https://leetcode.com/problems/reverse-bits/
# Difficulty: Easy
# Notes: 

# ---------------------------- #

# >>> My Solution <<<
# Time Complexity: 
# Space Complexity:
# Notes:

class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """

        # STEP 1: Convert to binary:
        res = ""
        while(n > 0):
            if n & 1 == 1:
                res = '1' + res 
            else:
                res = '0' + res 
            n = n >> 1

        # Pad out the left to make it 32 bit
        while len(res) < 32:
            res = "0" + res
        
        # STEP 2: LEFT => RIGHT, since we are reversing the number!
        i, num, power = 0, 0, 0
        while (i < len(res)):
            if (res[i] == '1'):
                num += pow(2,power)
            power += 1
            i += 1

        return num

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