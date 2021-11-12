class Person:
    
    def __init__(self,name,age,gender):
        self.name = name 
        self.age = age 
        self.gender = gender

    
class Student(Person):

    def drop_class():
        pass

    def study():
        pass
        
    def take_exams(): 
        pass
    
    def take_classes(self,take_class):
        self.take_class = take_class
        take_class = ["math", "algebra", "python"]
        if self.take_class == (str["math"]):
            return ("monday- math")
        if self.take_class == (str["algebra"]):
            return ("tuesday- algebra")
        if self.take_class == (str["python"]):
            return ("wednsday-python")



student1=Student()
student1.name = "Ali"
student1.age = 19
student1.gender = "male"
student1.take_clase = ["math", "python"]
display_schedule = student1.take_class()
print(student1.name, display_schedule)
 



    