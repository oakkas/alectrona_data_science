#p_4. Write a function that takes the base and height of a triangle and return its area.

print('Area of triangle calculator')
base=round(float(input('What is the base of your triangle in cm? ')),2)
height=round(float(input('What is the height of your triangle in cm? ')), 2)
area = round(float(base*height/2), 2)
print(f'Area of your choice triangle is {area}')