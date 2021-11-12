from abc import abstractclassmethod


def my_budget(number, by):
    return number+by


print(my_budget(1, 2))


def pearson(x):
    return 5/x


print(pearson(10))


def multiply(*numbers):
    x = 1
    for number in numbers:
        x *= number
    return x


print(multiply(2, 3, 4, 5))


def converted(*xs):
    mylist = []
    for x in xs:
        mylist.append(x*0.62)
    return mylist


mylist = converted(10, 20, 30)


def myfunc(x, y):
    return x+y


print(myfunc(-2, -5))


def addition(x):
    return 1 + x


print(addition(0))
print(addition(9))
print(addition(-3))


def convert(x):
    return 60*x


print(convert(5))
print(convert(3))
print(convert(2))


def tri_area(x, y):
    return x*y*0.5


print(tri_area(3, 2))
print(tri_area(7, 4))
print(tri_area(10, 10))


def next_edge(x, y):
    return x+y-1


print(next_edge(8, 10))
print(next_edge(5, 7))
print(next_edge(9, 2))


def stutter(x):
    print(x[0:2], "... ", x[0:2], "... ", x)


stutter("incredable")
stutter("enthusiastic")
stutter("outstanding")


def Discount(x, y):
    return x-(0.01*x*y)


print(Discount(1500, 50))
print(Discount(89, 20))
print(Discount(100, 75))


relation_to_luke = {
    "Darth Vader": "father",
    "Leia": "sister",
    "Han": "brother in law",
    "R2D2": "droid"
}
x = relation_to_luke. get("Leia")
print("Luke, I am your " + x)
print(relation_to_luke["Han"])


def number_length(x):
    y = str(x)
    print(len(y))


number_length(400)


class mammal:
    def __init__(self, name):
        self.name = name

    def zoo(self):
        print("hey mammals")


class dog(mammal):
    def zoo(self):
        print("dog talking")


d = dog("rockie")
d.zoo()


def fizz_buzz(x):

    if x % 15 == 0:
        return "FizzBuzz"
    elif x % 3 == 0:
        return "Fizz"
    elif x % 5 == 0:
        return "Buzz"
    else:
        return x


print(fizz_buzz(10))


def profit(x):
    profit = (x["sell_price"] - x["cost_price"])*x["inventory"]
    return profit


print(profit({"cost_price": 32.67, "sell_price": 45.00, "inventory": 1200}))


def aritmatic_operation(x):
    splits = x.split(" ")
    a = int(splits[0])
    operator = splits[1]
    b = int(splits[2])
    print(a)
    print(operator)
    print(b)
    if operator == "+":
        return a+b
    elif operator == "-":
        return a-b
    elif operator == "*":
        return a*b
    elif operator == "/":
        if b == 0:
            return -1
        else:
            return a/b


print(aritmatic_operation("11 / 0"))


print(range(1, 5))





def multiply(numbers):
    total=1
    for x in numbers:
        total*=x
    return total

x=([2,3,4,5])
print (multiply(x))


class triangle:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
    def perimeter(self):
        result = self.a+self.b+self.c
        return result

triangle1 = triangle(3,4,5)
p_cal= triangle1.perimeter()
print(p_cal)

        
class polygnal:
    def __init__(self,sides):
        self.sides=sides

    def perimtr(self):
        return sum(self.sides)

class rectangle(polygnal):
    def perimetr(self):
        print("triangle has 2 dimensiaol shape")     

rectangle1= rectangle([2,3,4,5])
r1= rectangle1.perimtr()
print(r1)

rectangle1.perimetr()

class Person:
    def__init__(self,name,age,gender):
    self.name = name 
    self.age = age 
    self.gender = gender

class Student(Person):
    def__init__(self, courses, schedule):
        self.courses=courses
        self.schedule = schedule
    def display_schedule(self,):
        schedule
