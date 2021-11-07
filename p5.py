#p_5. Create a function that finds the maximum range of a triangle's third edge, where the side lengths are all integers.

print('Possible longest side of your choice triangle')
side1=int(input('What is the first side of your triangle in cm? '))
side2=int(input('What is the second side of your triangle in cm? '))
maximum = int(side1+side2-1)
print(f'The maximum length of third side of your choice triangle is {maximum} cm')