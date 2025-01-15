# name = "XUV7OO"
# age = -25
# price = 25.7

# print(type(name))
# print(type(age))
# print(type(price))

# # inputs are always in form of string
# s_age = input("Enter your age:")
# print(s_age)
# print(type(s_age))

# a,b = 2,3
# # print(a)
# txt = '''@'''
# # print(type(txt))
# print(a*txt*b)#it will print @ six times cause 2*3 = 6 and then 6*@ = @@@@@@
#or

# a,b = "2",3
# txt = "@"
# print((a+txt)*b)

# name = "pratik"
# surname = "parmar"
# print(surname + name)

# a,b = 4,2 #the division of any numbers are always in float type
# c = a/b
# print(c)

# if we want to do division and want integer value there is one method called integer division 
# it gives answer of division in int that convered to float 
# a,b = 1.5,3
# c = a//b
# print(c, a/b)#expected answer should be 0.5 but actual answer is 0.0 cause it convert the answer in smallest round figer value
# print(type(c))

#floor mathod is same as integer division it also return equal or nearest smallest integer 
# a,b = 12,5
# c = a//b
# print(c)
# or 
# a,b = -12,5
# c = a//b
# print(c)
#or
# a,b = 12,-5
# c = a//b
# print(c)#expected answer is -2.4 but acutual answer is -3

#modulo expression
# a,b = 5,2
# c = a%b
# print(c)
#or
# a,b = -5,2
# c = a%b
# print(c)
#or modulo is nagitive only if denominator is nagitive,Like
# a,b = 5,-2
# c = a%b
# print(c)

#Taking inputs from users
# name = input("Enter your name:")
# age = int(input("Enter your age:"))
# price = float(input("Enter your price:"))

#code to find area of circle 
# pi = 3.14
# r = float(input("Enter radiuse of circle:"))
# area_circle = pi * r * r
# print(area_circle)

# type conversion // or // automatic conversion
# a,b = 2,4.25
# sum = a+b # 2.0 + 4.25
# print(sum)

#type casting // or // manual conversion
# a = "2"
# a = int("2") # convert
# b = "4.25"
# b = float("4.25")
# sum = a+b
# print(sum)
# print(type(a))
# print(type(b))

# practice question 
# input two numbers and print sum of them
# a = int(input("Enter first number = "))
# b = int(input("Enter second number = "))
# sum = a + b
# print(sum)

#practice question 
# Find area of square
# side = float(input("Enter the side of the square :"))
# area = side * side
# print("The area of the square is ", area)

#practice question
#input two values and print average of them
# num1 = float(input("Enter first value :"))
# num2 = float(input("Enter second value :"))
# avg = (num1 + num2)/2
# print("avarage :", avg)

#practice questions
#input two numbers and print true if first is greater than or equal to the second else false.
# num1 = float(input("Enter first value :"))
# num2 = float(input("Enter second value :"))
# print(num1 >= num2)


