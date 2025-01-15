#Conditional statements 

#Traffic Lights Code
# print("Traffic Lights")
# light = input("Enter Light color:")
# if(light == "red"):
#     print("Stop")
# elif(light == "green"):
#     print("Go")
# elif(light == "yellow"):
#     print("Look")
# else:
#     print("Lights are broken")

# #Grades of Students
# print("Grade of sudents")
# marks = int(input("Enter your marks:"))
# if(marks >= 90):
#     print("A")
# elif(marks >= 80 and marks < 90):
#     print("B")
# elif(marks >= 70 and marks < 80):
#     print("C")
# else:
#     print("D")
 
# #Practice #input a = 5 & g = m , a = 2 & g = f
# a = int(input("A :"))
# g = input("M/F:")
# if((a == 1 or a == 2) and g == "M"):
#     print("fee is 100")
# elif(a==3 or a==4 or g == "F"):
#     print("fee is 200")
# elif(a == 5 and g == "M"):
#     print("fee is 300")
# else:
#     print("no fee")

#Ternary Operator , single line conditional statements
# food = input("food :")
# # eat = "Yes" if food == "cake" else "No"
# # print(eat)
# #or
# print("Yes") if food == "cake" or food == "jalebi" else print("No")

#Clever if / ternary operator
# age = int(input("Enter your age: "))
# vote = ("NO","Yes") [age>18]
# print(vote)
# #or
# sal = int(input("Salary : "))
# tax = sal*(0.1,0.2) [sal > 50000]
# print(tax)

#practice question 
#wap to check the number is even ot odd
# num = int(input("Enter a number: "))
# if (num%2 == 0):
#     print("The number is even")
# else: 
#     print("The number is odd")

# #wap to find gretest of 3 numbers entered by the user
# num1 = int(input("Enter 1st number: "))
# num2 = int(input("Enter 2nd number: "))
# num3 = int(input("Enter 3rd number: "))
# #program for four numbers
# num4 = int(input("Enter 4th number: "))

# if(num1>num2 and num1>num3):
#     print("The 1st number",num1,"is gretest.")
# elif(num2>num3):
#     print("The 2nd number",num2,"is gretest.")
# else:
#     print("The 3rd number",num3,"is gretest.")
# #4 numbers
# if (num1>num2 and num1>num3 and num1>num4):
#     print("The 1st number",num1,"is gretest.")
# elif(num2>num3 and num2>num4):
#     print("The 2nd number",num2,"is gretest.")
# elif(num3>num4):
#     print("The 3rd number",num3,"is gretest.")
# else:
#     print("The 4th number",num4,"is gretest.")

#wap to check the number is multiple of 7 or not
num = int(input("Enter a number: "))

if (num % 7 == 0):
    print("The number is multiple of 7")
else:
    print("The number is not multiple of 7")