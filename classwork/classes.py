class Student:
    def __init__(self, name, course):
        self.name = name
        self.course = course
    
    def get_name(self):
        return self.name
    def get_course(self):
        return self.course
    def set_name(self, new_name):
        self.name = new_name
        return self.name
    def set_course(self, new_course):
        self.course = new_course
        return self.course
    def describe_student(self):
        return f"Student Name: {self.name} Course:{self.course} "
    
student1 = Student("Johan", "CYSE130")
print(student1.describe_student())