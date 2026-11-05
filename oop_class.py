# Student is the class, each student is an object, init is a constructor
class Student:
    # class attribute: 
    school_name = 'Lincoln HS'
    # instance attributes:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    #create a method inside a class
    def welcome(self):
        print('Welcome', self.name)

s1 = Student('John', 95)
s2 = Student('Jenny', 98)
s3 = Student('Emma', 85)
print(s1.name)
print(Student.school_name)
print(s2.school_name)
print(s1.marks)
print(s2.name)
print(s2.marks)
print(s3.name)
print(s3.marks)
s1.welcome()
s2.welcome()

class Student2:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def get_average(self):
        avg = sum(self.marks)/len(self.marks)
        print(self.name, "average: ", avg)

s1b = Student2('Emma', [99, 98, 97])
s2b = Student2('John', [75, 80])

s1b.get_average()
s2b.get_average()