## Class Methods: 
## 1. Allows operations related to the class itself
## 2. Takes cls or self as the first parameter

## Instance Methods = Best for operations on instances of the class (objects) -> use self
## Static Methods = Best for utility functions that do not need access to class data
## Class Methods = Best for class-level data or we require access to the class itself -> use cls

class Student:
    count = 0
    total_gpa = 0

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1
        Student.total_gpa += self.gpa

    ## Instance Method
    def get_info(self):
        return f"{self.name} {self.gpa}"
    
    ## Class Method
    @classmethod
    def get_count(cls):
        return f"Total # of students: {cls.count}"
    
    @classmethod
    def get_total_gpa(cls):
        return f"Total GPA of students: {cls.total_gpa}"
    
    @classmethod
    def get_average_gpa(cls):
        if cls.count == 0:
            return 0
        else:
            return f"Average GPA: {cls.total_gpa / cls.count:.2f}"


student1 = Student("Spongebob", 3.2)
student2 = Student("Patrick", 2.0)
student3 = Student("Sandy", 4.0)

# print(Student.get_count() )
# print(Student.get_total_gpa() )

print(Student.get_average_gpa())