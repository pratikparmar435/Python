#wap to print fizz if number is multiple of 3 and buzz if 5 and fizzbuzz if it is multiple of both
# for i in range(1,101):
#     if i % 3 == 0 and i % 5 == 0:
#         print("FizzBuzz")
#     elif i % 3 == 0:
#         print("Fizz")
#     elif i % 5 == 0:
#         print("Buzz")
#     else:
#         print(i)

#wap to print factorial of given number
# num = int(input("Enter a number to find factorial:"))
# num = abs(num)
# factorial = 1
# for i in range(2,num+1):
#     factorial *= i
# print("Factorial of your number is:",factorial)

#wap to print fibonacci sequence 
n = int(input("Enter a number:"))
a,b = 0,1
for i in range(n):
    print(a,end=" ")
    a,b = b,a+b