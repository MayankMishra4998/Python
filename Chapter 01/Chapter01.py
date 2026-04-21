print("Hello World")

name = "Mayank Mishra"
print(f"Hello {name}")
# This is a comment

age = 20
is_student = True
print(f"Name : {name} , Age: {age} , is Student: {is_student}")

if age >= 18:
    print(f"{name} is age is {age} , you are Adult")
else:
    print(f"{name} is age is {age} , you are Minor")



# Input from user
# user_name = input("Enter your name : ")
# user_age = int(input("Enter your age : "))
# print(f"Hello {user_name} , {user_age} year old , Welcome in Chapter 1")


# rec_lenght = float(input("Enter the length of rectangle : "))
# rec_br = float(input("Enter the br : "))

# area = rec_lenght * rec_br
# print (f"The area of rec = {area} \n  the rec is {rec_lenght} \n  the br is {rec_br}")

# Arithmetic Operators
a = 10
b = 3

# result = pow(a,b) means a^b =1000
# result = round(3.14159,2) means round the number to 2 decimal places = 3.14
# result = round(12.4)  means round the number to nearest integer = 12
# result = abs(-5) means absolute value of -5 = 5
# result = max(10,20,30) means maximum value among 10,20,30 = 30
result = min(10,20,30) # means minimum value among 10,20,30 = 10

print(f"result : {result}")


# if you want the mathmatical value 
import math

# a = 20.3
# print(math.pi) # 3.141592653589793
# print(math.e) # 2.718281828459045
# print(math.sqrt(a)) # if you want the square root of a = 4.47213595499958


# radius = float(input("Enter the radius : "))
# radius1 = float(input("Enter the radius : "))
# area = 2 * math.pi * float(radius)
# print(f"The Circumference of circle with radius {radius} is {round(area, 2)}")
# print(f"the hypotenuse of right angle triangle {round(pow(pow(radius , 2) + pow(radius1 , 2), 1/2),2)} ")


