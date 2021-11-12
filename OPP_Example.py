
#1. Let's create a person class which has name, age, gender attributes.
#2. Using above person class, create a student class. It has all the attributes from person,
#  and courses, schedule attributes. Student takes and drop courses, study, take exam. When asked student can display his/her schedule. 
# 3. Create a course class with attributes description, credit and course_schedule, exam_schedule, instructor. One should be able to display course schedule and other info seperatelly. 
#4. Create an instructor class from Person. In addition to attributes from person, it has courses, schedule, rating attributes. Instructor can open a new course. When asked instructor can display his/her schedule.
#5. Create an instance of instructor, student. Have instructor create a course (maybe Python), and studnet takes the course. Create another instructor with Math course and student takes that one as well. 
#6. Display student's current schedule.

   


class Person:
    
    def __init__(self, name, age, gender) :
        self.name = name 
        self.age = age 
        self.gender = gender

    
class Student(Person):       
    def __init__(self,name, age, gender, courses, schedule):
        super().__init__(name, age, gender)
        self.courses=courses
        self.schedule = schedule

    def take_course(self, new_course):
        self.courses.append(new_course)

    def drop_course(self, drop_course):
        self.courses.remove(drop_course)

    def studies(self, study):
        self.study = study
        
    def take_exams(self, exam): 
        self.exam = exam

    def display_schedule(self):
        for course in self.courses:
            print(course.description +" : "+ course.course_schedule)
       

class Course:
    def __init__(self,description,credit, course_schedule, exam_schedule, instructor):
        self.description = description
        self.credit = credit
        self.course_schedule = course_schedule
        self.exam_schedule = exam_schedule
        self.instructor = instructor



class Instructure(Person):
    def __init__(self, name, age, gender,course, schedule, rating):
        super().__init__(name, age, gender)
        self.course= course
        self.schedule = schedule
        self.rating = rating

    def set_course(self,course):
        self.course = course  

    def display_schedule(self):
        pass

#5. Create an instance of instructor, student. Have instructor create a course (maybe Python),
#  and studnet takes the course. Create another instructor with Math course and student takes that one as well. 

instructure1 = Instructure("robert", 34, "male", "", "", 9)
student1=Student("Ali", 19, "male", [], "")

python_course= Course("python",10, "weds 10-12 am", "", instructure1)
instructure1.set_course(python_course)
student1.take_course(python_course)

instructure2= Instructure ("mike",39, "male", "","", 9)
math_course= Course("math", 10, "tues 10-12 am" , "", instructure2)
instructure2.set_course(math_course)
student1.take_course(math_course)

#6. Display student's current schedule.
student1.display_schedule()








