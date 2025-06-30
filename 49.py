# LeetCode link: https://leetcode.com/problems/group-anagrams/description/
# Difficulty: Medium
# Notes: 
# Good question to work on the fundamentals
    # Inefficent solution take-aways:
        # Learn off by heart how to sort, join, separate strings, etc!
    # Efficient solution take-aways:
        # ord() is used to find ascii
        # Lists are not hashable since they are mutable
        # Tuples are the mutable versions of lists
        # 'defaultdict' from collections can be used to avoid keyErrors. defaultdict(list) removes the need to create an empty list for each key of the hashmap!

# ---------------------------- #

# >>> My Solution -> Sorting <<<
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

# >>> Soluton using Neet's explanation <<<
# Time Complexity: o(m*n*26) == O(m*n)
    # Use Hashmap to keep track of strings that have the same letter count for all letters.
    # For example, 'eat' and 'tea' have 1 'e', 1 'a' and 1 't'!
    # n = number of input strings 
    # m = average length of strings
    # 26 = number of letters in alphabet
# Space Complexity: 
# Notes: More time efficient solution but can be improved

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        res = {}

        for string in strs:

            count = [0]*26 # a...z

            for char in string:
                #ascii of 'a' is 97.
                # We want 'a' to be index 0 in our 'count' list, and so on.
                count[ord(char) - 97] += 1
            
            # Convert our 'count' list to a tuple, since lists are NOT hashable (since they are mutable).
            if tuple(count) in res:
                res[tuple(count)].append(string)
            else: res[tuple(count)] = [string]
        
        return res.values() #We don't care about the keys



# ---------------------------- #

# >>> Neet Final <<<
# Time Complexity: See above
# Space Complexity: 
# Notes:

from collections import defaultdict 

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        res = defaultdict(list)

        for string in strs:
            count = [0]*26

            for char in string:
                count[ord(char) - ord('a')] += 1
            
            # We use 'defaultdict' with a default value type of 'list'
            # This helps us to avoid manually checking to see if each key already exists.
            res[tuple(count)].append(string)
        
        return res.values()
# ---------------------------- #

# >>> : <<<
# Time Complexity:
# Space Complexity: 
# Notes: