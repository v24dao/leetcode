### -- Introduction -- ###

# Learning Python won't be too hard if you are familiar with another language
# It is worth learning Python JUST for coding interviews
# Neet hasn't written a single line of Python for any of this jobs, yet he interviewed in Python 

### -- Variables -- ###

## Variables are dynamically typed:

# n = 0
# print ('n =', n)

# n = "abc"
# print('n =', n)

## Multiple Assignments:

# n, m = 0, "abc"
# n, m, z = 0.125, "abc", False

## Increment: 
# n = n + 1
# n += 1 
# n++ #(can't do this!) 

## None is null (absence of a value)
# n = 4
# n = None
# print("n = ", n)

### -- If Statements -- ###

## If statements don't need parentheses or curly braces:
# n = 1
# if n > 2:
#     n -= 1
# elif n == 2:
#     n *= 2
# else:
#     n += 2

## Parentheses needed for multi-line conditions:

# and = &&
# or = ||

# n, m = 1, 2
# if ((n > 2 and 
#      n!= m) or n == m):
#      n += 1


### -- Loops -- ###

## While loops are similar:

# n = 0
# while n < 5:
#    print(n)
#    n += 1 

## Looping from i = 0 to i = 4
# for i in range(5):
#     print(i)

## Looping from i = 2 to i = 5
# for i in range(2,6):
#     print(i)

## Looping from i = 5 to i = 2
# for i in range(5,1, -1):
#     print(i)

## Note: range(start(inclusive),end(non-inclusive),increment)
### -- Math -- ###

## Division is decimal by default (unlike other programming languages):
# print(5/2) # Outputs 2.5

## Double slash `rounds down`:
# print(5//2) # Outputs 2

##CAREFUL: Most languages will round towards 0 by default, so negative numbers will round down (instead of towards 0):
# print(-3//2) # Outputs -2 (-3 divided by 2 = -1.5, rounded down to 2)

##A workaround for rounding towards zero is to use decimal division and then convert to int:
# print(int(-3/2)) # Outputs -1 (-3 divided by 2 = -1.5, -1.5 is converted to the int -1)

## Modding is similar to most languages:
# print(10 % 3) #outputs 1 (as expected)

## Except for negative values:
# print(-10 % 3) # outputs 2 (unexpected)

## To be consistent with other languages modulo:
import math
# print(math.fmod(-10,3)) #Outputs -1.0 as expected

## More Math helpers:
# print(math.floor(3 / 2))
# print(math.ceil(3 / 2))
# print(math.sqrt(4))
# print(math.pow(2,3))

## Max/ Min Int:
# float("inf")
# float("-inf")

## Python numbers are infinite so they never overflow:
# print(math.pow(2,200)) #very big number

## This very big number is still less than infinity:
# print(math.pow(2,200) < float("inf")) #True

### -- Arrays -- ###

## Arrays are called 'lists' in Python:

# arr = [1,2,3]
# print(arr)

## Arrays in Python are dynamic arrays by default.

## They can be used as a stack:
# arr.append(4) # O(1) / constant time
# arr.append(5)
# print(arr) #[1,2,3,4,5]
# arr.pop() # O(1) / constant time
# print(arr) #[1,2,3,4]

## We can insert into an array, because this is technically an array, and not a stack:
# arr.insert(1,7) # O(n)
# print(arr) #[1,7,2,3,4]

## Initialise an arr of size n with default value of 1:
# n = 5
# arr = [1] * n
# print(arr) #[1,1,1,1,1]
# print(len(arr)) #5

## Careful: -1 is not out of bounds in Python, it's the last value:
# arr = [1,2,3]
# print(arr[-1]) #3

## Sublists (aka slicing), last index is non-inclusive:
# arr = [1,2,3,4]
# print(arr[1:3]) #[2,3]

## Similar to for-loop ranges, last index is non-inclusive:
# print(arr[0:4])

##Unpacking: 
# Be careful... number of variables on LHS has to match number of elements in array!
# a,b,c = [1,2,3]
# print(a,b,c)

##Loop through arrays:
# nums = [1,2,3]

## Using Index:
# for i in range(len(nums)):
#     print(nums[i])

## Without index:
# for n in nums:
#     print(n)

## With index AND value:
# for i, n in enumerate(nums):
#     print(i, n)

## Loop through multiple arrays simultaneously with unpacking:
# nums1 = [1,3,5]
# nums2 = [2,4,6]

# for n1, n2 in zip(nums1,nums2):
#     print(n1,n2)

## Reversing an array:
# nums.reverse()
# print(nums)

### -- Sorting -- ###

## Sorting Numbers: By default, array is sorted in ascending order
# arr = [5,4,7,3,8]
# arr.sort()
# print(arr)

## Sorting in reverse:
# arr.sort(reverse=True)
# print(arr) # [8,7,5,4,3]

## Sorting Strings: By default, array is sorted in alphabetical order
arr = ["bob", "alice", "jane", "doe", "boo"]
# arr.sort()
# print(arr) #['alice', 'bob', 'boo', 'doe', 'jane'] 

## Custom sort (by length of string):
# arr.sort(key=lambda x: len(x), reverse=True)
# print(arr) #['alice', 'jane', 'bob', 'boo', 'doe']

### -- List Comprehension -- ###
# arr = [i for i in range(5)] #[0,1,2,3,4]
# print(arr)
# arr = [i*i for i in range(5)] #[0,1,4,9,16]
# print(arr)

### -- 2D Arrays -- ###

## Easiest way to do it:
# arr = [[0] * 4 for i in range(4)] #[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
# print(arr)

## This won't work as intended: All 'rows' are identical!
# arr = [[0] * 4 ] * 4
# arr[1][0] = 1 # We get [[1, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0]]
# print(arr) 
## Not only does arr[1][0] change... so does: arr[0][0], arr[2][0], arr[3][0]

### -- Strings -- ###

## Pretty similar to arrays:
# s = "abc"
# print(s[0:2]) #'ab'

## But they are immutable
##
## (line below produces a TypeError)
# s[0] = "A"

## Updating a string:
## This creates a new string! Anytime you modify a string, it's considered an n time operation.
# s += "def"

## Valid numeric strings can be converted:
# print(int("123") + int("123")) #246

## And numbers can be converted to strings:
# print(str(123) + str(123)) #123123

## In rare cases, you may need the ASCII value of a char:
# print(ord("a")) #97
# print(ord("b")) #98

## Combine a list of strings, with a 'delimitor':
# strings = ["ab", "cd", "ef"]
# print(",".join(strings))

### -- Queues -- ###
## In Python, queues are double ended by default.
## We can import them.
from collections import deque

# queue = deque()
# queue.append(1)
# queue.append(2)
# print(queue) #[1,2]

## Our queue isn't much different from a stack.
## However, the advantage is that we can pop from the left of the queue, in constant time!
## We cannot do this with a stack!

# queue.popleft()
# print(queue) #[2]

## We can also add values back to the left side!
# queue.appendleft(1)
# print(queue) #[1,2]

## We can ofcourse pop from the RHS too:
# queue.pop()
# print(queue) #[1]

### -- Hash Sets -- ###
## Can search, add and remove values in constant time:

# mySet = set()

##Add:
# mySet.add(1)
# mySet.add(2)
# print(mySet) # {1,2}
# print(len(mySet)) # 2

##Search:
# print(1 in mySet) #True
# print(2 in mySet) #True
# print(3 in mySet) #False

##Remove:
# mySet.remove(2)
# print(2 in mySet) #False

##Initialising a set with list:
# print(set([1,2,3])) #{1,2,3}

## Set comprehension:

# mySet = {i for i in range(5)} #{0,1,2,3,4}

### -- Hash Maps -- ### 
## Most common data structure / AKA 'dict'
myMap = {}
## Assigning value of a key:
# myMap["alice"] = 88
# myMap["bob"] = 77
# print(myMap) # {"alice": 88, "bob": 77}
# print(len(myMap)) #2

## Modifying value of a key:
# myMap["alice"] = 80
# print(myMap) # {"alice": 80, "bob": 77}

##Check if a key exists:
# print("alice" in myMap) #True
# print("warra" in myMap) #False

##Pop:
# myMap.pop("alice")
# print("alice" in myMap) #False

##Initialising Hash Maps:
# myMap = {"alice": 90, "bob": 70}
# print(myMap)

## Dict Comprehension: Common for graphing questions:
# myMap = {i: 2*i for i in range(3)}
# print(myMap)

## Looping through map - Method 1:
# myMap = {"alice": 90, "bob": 70}
# for key in myMap: 
#     print(key, myMap[key])

## Looping through map - Method 2:
## Directly looping through maps (situations where we don't need a key)
# for val in myMap.values():
#     print(val)

## Looping through map - Method 3:
## Unpacking:
# for key, val in myMap.items():
#     print(key, val)

### -- Tuples -- ###
##Tuples are like arrays but immutable:
tup = (1,2,3)
# print(tup) #{1,2,3}

## We can index them:
# print(tup[0]) #1
# print(tup[-1]) #3

## We CANNOT modify them: Line below does NOT work.
# tup[0] = 0

## Main purpose of Tuples is to be used as key for hash map/set:
## Our (1,2) tuple is a 'hashable key'!
myMap = {(1,2): 3}
# print(myMap)

mySet = set()
mySet.add((1,2))
# print((1,2) in mySet) #True

## Lists CANNOT be keys:
# myMap[[1,2]] = 5 #Doesn't work

### -- Heaps -- ###
## Common Data Structure to find min/max of set of values (frequently).
##In python, heaps are implemented with arrays.
import heapq
## Under the hood are arrays:
# minHeap = []
# heapq.heappush(minHeap, 3)
# heapq.heappush(minHeap, 2)
# heapq.heappush(minHeap, 4)

## Min is always at index 0:
# print(minHeap[0]) #2

## Looping through heap and popping values:
# print("Looping through heap and popping values:")
# while len(minHeap):
    # print(heapq.heappop(minHeap))
##2,3,4 (smallest to largest, since minHeap)

## Max Heaps:
## There are no max heaps by default. The workaround is to use min heap and multiply by -1 when push and pop.
# maxHeap = []
# heapq.heappush(maxHeap, -3)
# heapq.heappush(maxHeap, -2)
# heapq.heappush(maxHeap, -4)

##Max is always at index 0:
##However, we have to multiply by -1 to negate the original -1.
# print(-1* maxHeap[0]) #4

# while len(maxHeap): 
#     print(-1 * heapq.heappop(maxHeap))

##4,3,2

##Build Heap from initial values:

# arr = [2,1,8,4,5]
# heapq.heapify(arr)
# while arr:
#     print(heapq.heappop(arr))
##1,2,4,5,8

### -- Functions -- ###

# def myFunc(n,m):
#     return n*m

# print(myFunc(3,4)) #12


### -- Nested Functions -- ###

##VERY USEFUL FOR CODING INTERVIEWS:

## Nested functions have access to outer variables:
def outer(a,b):
    c = "c"
    def inner():
        return a + b + c
    return inner()
    
# print(outer("a","b")) #abc

## Can modify objects but not reassign values
## unless using nonlocal keyword
## This trips a lot of people up! 
def double(arr, val):
    def helper():
        ## Modify array works:
        for i, n in enumerate(arr):
            arr[i] *= 2

        ## will only modify val in the helper scope
        # val *= 2

        ## declaring 'nonlocal'
        ## this will modify val outside helper scope
        nonlocal val 
        val *= 2
    helper()
    # print(arr,val)

nums = [1,2]
val = 3
double(nums, val)

##The above is just a trivial example.

### -- Classes -- ###

## Pretty concise, but limited compared to other languages.

class MyClass:
    ## Constructor in python is `__init__`
    ## `self` is passed into every method of a class. 
    ## It is basically the same as `this` in languages such as JavaScript
    def __init__(self,nums):
        #Create member variables
        self.nums = nums
        self.size = len(nums)

    #self key word required as a param
    def getLength(self):
        return self.size
    
    def getDoubleLength(self):
        return 2* self.getLength()

## TODO: Reformat and print out.