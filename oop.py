# Activity 1
class Student:
    def __init__(self, name, age, student_id):
        self.name = name
        self.age = age
        self.student_id = student_id

    def __str__(self):
        return f"Student(Name: {self.name}, Age: {self.age}, ID: {self.student_id})"

s1 = Student("Alice", 20, "S12345")
print(s1)
    
# Inheritance Example
class TeachingAssistant(Student):
    def __init__(self, ta_id, name, age, student_id):
        super().__init__(name, age, student_id)
        self.ta_id = ta_id

    def __str__(self):
        return f"TeachingAssistant(TA ID: {self.ta_id}, Name: {self.name}, Age: {self.age}, Student ID: {self.student_id})"
    
    def classes(self):
        return ["Web Development", "Data Science", "Machine Learning"]
    
    def assigned_classes(self):
        return ["Web Development", "Data Science"]
    
ta1 = TeachingAssistant("TA4523", "Alice", 20, "S12345")
a_classes = ta1.assigned_classes()
print(ta1)
print("Assigned Classes:", a_classes)

# Activity 2
# Polymorphism Example
class Car:
    def __init__(self, model, year):
        self.model = model
        self.year = year
    
    def move(self):
        print("Driving")


class Airplane:
    def __init__(self, model, year):
        self.model = model
        self.year = year
    
    def move(self):
        print("Flying")

class Boat:
    def __init__(self, model, year):
        self.model = model
        self.year = year

    def move(self):
        print("Sailing")
