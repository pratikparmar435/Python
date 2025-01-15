#function

# def print_helo():
#     print("Hello")
# print_helo()

# def calc_sum(a,b):
#     sum = a + b
#     print(sum)
# ans = calc_sum(2000,53)
# print(ans)

#find avg of 3 numbers
# def find_avg(a,b,c):
#     avg = (a+b+c)/3
#     return avg
# print(find_avg(1,2,3))

# def cal_prod(a,b):
#     return a*b
# print(cal_prod(int(input("Enter a first number")),int(input("Enter a second number"))))
#or
# num1 = int(input("Enter first number:"))
# num2 = int(input("Enter second number:"))
# print(cal_prod(num1,num2))

#default parameters in python 
# def cal_prod(a=1, b=1):
#     return a*b
# print(cal_prod())#output will be 1 because be set default values to out parameters 

#for example we can create function like range
# def prt_range(a,b,c=1):
#     while(a<b):
#         print(a)
#         a+=c
# prt_range(1,10)
# prt_range(1,10+1)
# prt_range(1,10,2)#this we give a number of steps to print
# prt_range(2,11,2)#this we give a number of steps to print

#practice questions 
#create function that's find the length of our list 
# cities = ["bantwa","manavadar","vadala","Harshd","Ahemdabad"]
# names = ["pratik","dhaval","samat","aadity","divyash"]
# def print_len(list):
#     print(len(list))
# print_len(cities)
# print_len(names)

#waf to print element of a list in a single line
# cities = ["bantwa","manavadar","vadala","Harshd","Ahemdabad"]
# def eleInLine(list):
#     for i in list:
#         print(i,end=" ")
# eleInLine(cities)

#waf to find factorial of n number
# def find_fac(num):
#     factorial = 1
#     i = 1
#     while(i<=num):
#         factorial *= i
#         i += 1
#     print("The factorial with while loop is:",factorial)
# #or with for loop
# def find_fac2(num):
#     factorial = 1
#     for i in range(1,num+1):
#         factorial *= i
#     print("The faoctorial with for loop is:",factorial)
# find_fac(4)
# find_fac2(4)

#waf to convert USD to INR
# def convert_INR(USD):
#     INR = 83 * USD
#     print(USD,"USD =",INR,"INR")

# convert_INR(10)

#waf to print number is even or odd
# def chkEvenOdd(num):
#     if(num % 2 == 0):
#         print("Even")
#     else:
#         print("Odd")
# chkEvenOdd(20)
# chkEvenOdd(15)

#Recursion

# def show(n):
#     if n == 0:
#         return
#     print(n)
#     show(n-1)

# show(5)

# find factorial of number using recursion
# def find_fact(n):
#     if n == 0 or n == 1:
#         return 1
#     return find_fact(n-1) * n
# print(find_fact(5))

#wap to find sum of first n numbers
# def sum(n):
#     if n == 0:
#         return 0
#     return sum(n-1) + n
# print(sum(5))
#or
def sum(n):
    if (n>0):
        result = sum(n-1) + n
    else:
        result = 0
    return result
print(sum(6))