#program to check if number is odd print all odd numbers from 0 to num and if number is even print all even
#numbers from 0 that number
# num = int(input("Enter a number to check even or odd:"))
# if num % 2 == 0:
#     print(f"The number {num} is even")
#     for i in range(0,num+1):
#         # print(i)
#         if i % 2 == 0:
#             print(i)
# else:
#     print(f"The number {num} is odd")
#     for i in range(1,num+1):
#         # print(i)
#         if i % 2 != 0:
#             print(i)



#sum of digits
#wap to take integer as input and print sum of it's digits 
# num = int(input("Enter digits to find their sum:"))
# num_to_string = str(num)
# sum = 0
# for i in num_to_string:
#     i = int(i)
#     sum = sum + i
# print(sum)



#program to fizzbuzz game
# for num in range(1,51):
#     if num % 3 == 0 and num % 5 ==0:
#         print("FizzBuzz")
#     elif num % 5 == 0:
#         print("Buzz")
#     elif num % 3 == 0:
#         print("Fizz")
#     else:
#         print(num)



#write a program to check if the number is prime number or not
# num = int(input("Enter a number to check if it is prime or not:"))
# isPrime = True

# for i in range(2,num):
#     if num % i == 0:
#         isPrime = False

# if isPrime:
#     print("The number is prime number")
# else:
#     print("The number is not prime number")