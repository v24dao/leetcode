# Link: https://neetcode.io/problems/insertionSort
# Difficulty:
# Notes: 

# ---------------------------- #

# >>> My Solution <<<
# Time Complexity: 
# Space Complexity:
# Notes:

# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
import copy
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        ans = [copy.deepcopy(pairs)]
        for i in range(1,len(pairs)):
            j = i - 1
            # Condition for swapping elements
            while pairs[j+1].key < pairs[j].key and j>=0:
                temp = pairs[j]
                pairs[j] = pairs[j+1]
                pairs[j+1] = temp
                j -= 1
            ans.append(copy.deepcopy(pairs))
        return ans
# ---------------------------- #

# >>> Neet's more pythonic solution <<<
# Time Complexity:
# Space Complexity: 
# Notes:

# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        n = len(pairs)
        res = [] #intermediate states

        for i in range(n):
            j = i - 1

            # Condition for swapping:
            while j >= 0 and pairs[j].key > pairs[j+1].key:
                pairs[j], pairs[j + 1] = pairs[j + 1], pairs[j]
                j -= 1

            res.append(pairs[:]) #Create and append a shallow copy

        return res 
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