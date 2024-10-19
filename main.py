import math
import time
#variables
# first_name = 'Byrone'

# print(f"Hello {first_name}")

# is_student = True

#if-statement

# if is_student:
    # print("You are a student")
# else:
    # print("You are not a student")

#type-casting

# name = "Byrone Kingsly"
# age = 20
# gpa = 3.2

#type-cast from float to int

# gpa = int(gpa)

# print(gpa)

#checkin type of variable
# print(type(name))

# Prompting input values and displaying the value

# names = input("What is your name? ")

# print(f"Hello, {names}")

# Area of a rectangle from user input exercise
#
# length = int(input("Length of rectangle: "))
#
# width = int(input("Width of rectangle: "))
#
# print(f"Area of rectangle: {length * width}cm")

# Incrementing and decrementing
# friends = 0
# incrementing
# friends+= 1

# decrementing
# friends-= 1

# Circumference of a circle

# radius = float(input("Enter Radius of circle: "))

# circumference = 2 * math.pi * radius
#
# print(f"Circumference of circle of radius {radius} is : {circumference}")

# Area of a circle

# radius = float(input("Enter Radius of circle: "))
#
# area = math.pi * math.pow(radius, 2)
#
# print(f"Area of circle of radius {radius} is {area}: ")


# Hypotenuse of a right-angled triangle


# height = float(input("Enter  height : "))
#
# base = float(input("Enter  base : "))
#
# hypotenuse = math.sqrt(math.pow(base,2)+math.pow(height,2))
#
# print(f"The hypotenuse of right-angled triangle of base {base} and height {height} is {hypotenuse}")


# Simple calculator

# num1 = float(input('Enter first Number: '))
# operator = input('Enter operator: ')
# num2 = float(input('Enter second Number: '))
#
# if operator == '+':
#     result = num1 + num2
#     print(round(result,2))
# elif operator == '-':
#     result = num1 - num2
#     print(round(result,2))
# elif operator == '*':
#     result = num1 * num2
#     print(round(result,2))
# elif operator == '/':
#     result = num1 / num2
#     print(round(result,2))
# elif operator == '%':
#     result = num1 % num2
#     print(round(result,2))
# else:
#     print(f'{operator} is an Invalid Operator')


# if_else ternary operator (short_cut):

# age = 14
#
# print('Adult' if age >= 18 else 'Child')

# While loop

# name = input("Enter your name: ")
#
# while name == '':
#     print("You did not enter your name")
#     name = input("Enter your name: ")
#
# print(f"Hello {name}")

# Compound interest

# principle = 0
# rate = 0
# time = 0
#
# while principle <= 0:
#     principle = float(input("Enter your principle: "))
#     if principle <= 0:
#         print('Principle must be greater than zero')
#
# while rate <= 0:
#     rate = float(input("Enter your rate: "))
#     if rate <= 0:
#         print('rate must be greater than zero')
#
# while time <= 0:
#     time = float(input("Enter your time in years: "))
#     if time <= 0:
#         print('time must be greater than zero')
#
# total = principle * pow((1 + rate/100),time)
#
#
# print(f"The amount accrued is {total: .2f}")


# Count down timer

my_time = int(input("Enter the time in seconds: "))

for x in range(my_time,0,-1):
    seconds = x % 60
    minutes = int(x / 60) % 60
    hours = int(x / 3600)

    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)

print('YOU ARE DEAD!!!💣💣💣💣')