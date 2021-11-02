def my_budget(number,by):
    return number+by
print (my_budget(1,2))

def pearson(x):
    return 5/x
print(pearson(10))

def multiply(*numbers):
    x = 1
    for number in numbers:
        x*=number
    return x

print(multiply(2,3,4,5))


def converted(*xs):
    mylist = []
    for x in xs:
        mylist.append(x*0.62)
    return mylist

mylist = converted(10, 20, 30)

def myfunc(x,y):
    return x+y

print(myfunc(-2,-5))


def addition(x):
    return 1 +x

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

print (tri_area(3, 2))
print (tri_area(7, 4))
print (tri_area(10, 10))

def next_edge(x, y):
    return x+y-1
print (next_edge(8, 10))
print (next_edge(5, 7))
print (next_edge(9, 2))


def stutter(x):
  print (x[0:2] , "... ", x[0:2], "... ",x)
stutter("incredable")
stutter("enthusiastic")
stutter("outstanding")

