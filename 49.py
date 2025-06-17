# LeetCode link:
# Difficulty: Medium
# Notes: 
# Learn off by heart how to sort, join, separate strings, etc!

# ---------------------------- #

# >>> My Solution <<<
# Time Complexity: 
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