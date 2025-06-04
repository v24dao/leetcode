# LeetCode link: https://leetcode.com/problems/number-of-students-unable-to-eat-lunch/
# Difficulty: Easy
# Notes: 

# ---------------------------- #

# >>> My Solution <<<
# Time Complexity: O(n^2) => n = number of students. We have to rotate  through each sandwich up to n times. 
# Space Complexity: 0(1)
# Notes: 
class Solution(object):
    def countStudents(self, students, sandwiches):
        """
        :type students: List[int]
        :type sandwiches: List[int]
        :rtype: int
        """
        not_eaten = len(students)
        count = 0 #rotations without sandwich taken
        while students and count < len(students):
            if students[0] == sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)
                not_eaten -= 1
                count = 0
            else:
                students.append(students.pop(0))
                count += 1 #1 rotation without sandwich taken
        # if we rotate through all students, and no sandwich is taken.. return
        return not_eaten

        

# ---------------------------- #

# >>> Neet Solution - Uses Hashmap <<<
# Time Complexity: 0(n + n) => O(n)
# Space Complexity: O(1)
# Notes:

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        cant_eat = len(students)
        cnt = {1:0,0:0} #sandwich preferences

        # Update sandwich preferences in hashmap:
        for sandwich in students:
            if sandwich not in cnt:
                cnt[sandwich] = 0
            cnt[sandwich] += 1
        # Check if any students prefer the next remaining sandwich:
        for sandwich in sandwiches:
            # No students prefer the next remaining sandwich.
            if cnt[sandwich] == 0:
                return cant_eat
            # Student takes the next remaining sandwich. decrement variables:
            else:
                cant_eat -= 1
                cnt[sandwich] -= 1
        # This returns 0, since we have reached the end of sandwiches array!
        return cant_eat


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