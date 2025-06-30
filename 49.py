# LeetCode link: https://leetcode.com/problems/group-anagrams/description/
# Difficulty: Medium
# Notes: 
# Good question to work on the fundamentals
# Learn off by heart how to sort, join, separate strings, etc!

# ---------------------------- #

# >>> My Solution <<<
# Time Complexity: O(n*klogk) 
# n = number of strings, k = average length. Sorting 1 string of length k takes klogk. We do this n times!
# Space Complexity:
# Notes:
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        Hashmap = {}
        for s in strs:
            sorted_s = ''.join(sorted(s))
            if sorted_s not in Hashmap:
                Hashmap[sorted_s] = []
            Hashmap[sorted_s].append(s)
        
        return [Hashmap[x] for x in Hashmap]

# ---------------------------- #

# >>> : <<<
# Time Complexity: o(m*n*26) == O(n*k)
# Space Complexity: 
# Notes:
# n = number of input strings, k = average length of strings,26 = number of letters in alphabet



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