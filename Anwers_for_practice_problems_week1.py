
#p_1.
def addition(x,y):   # problem 1
    sum = x + y
    return sum


print(addition(-2,-5))

##################
#p_2.
def addition(parameter):   # problem 2
    return parameter + 1


print("addition " +str(addition(-3)))
##################
#p_3.

def convert(n):   # problem 3
    second = (n*60)
    return second


print(str(convert(10)) + " seconds")

##################
#p_4.

h = int()
b = int()


def tri_area( h, b):       # problem 4
    area = ((h * b)/2)
    return area


print("area of the triangle = " , (tri_area(10,20)))
##################
#p_5.                            # problem 5
def next_edge(a, b):
    c =(a+b)-1
    return c


print("max_length is " + str(next_edge(8, 10)))
##################
#p_6.

def stutter (my_word):       # problem 6
    my_ellipsis = "... "
    question_mark = "?"
    first_two = my_word [:2]
    my_pattern = first_two + my_ellipsis
    result = my_pattern + my_pattern + my_word + question_mark

    return result


print(stutter("incredible"))
##################
#p_7.
def dis(org_price, percent):                # problem 7
    final_price = int(org_price-(org_price*percent/100))
    return final_price

print(int(dis(1500, 50)))
##################
#p_8.
def relation_to_luke(relation):             # problem 8
    if relation == "Darth Vader":
        print("Luke, I am your father.")
    else:
        if relation == "Leia":
            print("Luke, I am your sister.")
        else:
            if relation == "Han":
                print("Luke, I am your brother in law.")
            else:
                if relation == "R2D2":
                    print("Luke, I am a droid.")

relation_to_luke("R2D2")

##################
#p_9.

##################
#p_10.

##################
#p_11.

for num in range(1, 51):                 # problem 11
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)



