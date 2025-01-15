# #While loops
# count = 1
# while count <=10000:
#     print("Hello",count)
#     count += 1

# #print numbers 1 to 5 
# i = 1
# while i <= 5:
#     print(i)
#     i+=1    
# print("loop ended")

# #print numbers 5 to 1
# j = 5
# while j>=1:
#     print(j)
#     j-=1
# print("loop ended")

#practice questions

#wap to print 1 to 100
# i = 1
# while i <= 100:
#     print(i)
#     i+=1

#wap to print 100 to 1
# i = 100
# while i>=1:
#     print(i)
#     i-=1

#wap to create multiplication table of number n
# n = int(input("Enter a number for table:"))
# i = 1
# while i <=10:
#     print(f"{n} * {i} = {n*i}")
#     i+=1

#wap to print all elements of list 
# mylist = [1,4,9,16,25,36,49,64,81,100]
# i = 0
# while i<len(mylist):
#     print(mylist[i])
#     i+=1

#search for number x in given tuple
# mytup = (1,4,9,16,25,36,49,64,81,100)
# x = 36
# i = 0
# while i<len(mytup):
#     if mytup[i] == x:
#         print("found at index",i)
#         br
#     else:
#         print("finding...")
#     i +=1
    
#Break keyword
# i = 1
# while i <=5:
#     print(i)
#     if (i == 3):
#         break
#     i+=1

#continue keyword
# i = 1
# while i <= 5: 
#     if (i == 3):
#         i +=1
#         continue#this will skip 3
#     print(i)
#     i+=1

#wap to print only odd values from 1 to 10
# i = 1
# while i <= 10:
#     if(i%2==0):
#         i+=1
#         continue
#     print(i)
#     i+=1
    
#For loop
# list = [1,2,3,4,5]
# for nums in list:
#     print(nums)
# str = "Parmar pratik"
# # str = str.replace(" ","")
# for char in str:
#     print(char)

#else with for loop
# str = "Parmar pratik"
# str = str.replace(" ","")
# for char in str:
#     print(char)
# else:#do some work when the for loop ends
#     print("End")

#questions
#wap to print values of given list
# list = [1,4,9,16,25,36,79,64,81,100]
# for val in list:
#     print(val)

#wap to search x value in given tuple
# tup = (1,4,9,16,25,36,79,64,81,100)
# find_num = int(input("Enter any number that you want to find:"))
# idx = 0
# for i in tup:
#     if find_num == i:
#         print("Found on index:",idx)
#     i += 1
# else:
#     print("Not Found!")

#Range function in for loop
# value = range(5)
# print(value)
# print(value[0])
# print(value[1])
# print(value[2])
# print(value[3])
# print(value[4])

#or we can use loop
# for val in value:
#     print(val)#the output will be 0,1,2,3,4
# or
# for val in range(5):#range(stop)
#     print(val)
#or
# for val in range(1,10):#range(start,stop)
#     print(val)
#or
# for val in range(1,10,2):#range(start,stop,step)
#     print(val)

#for example wap to print even numbers from 1 to 10
# for i in range(2,11,2):
#     print(i)

#practice questions
#wap to print 1 to 100
# for i in range(1,101):
#     print(i)

#wap to print 100 to 1
# for i in range(100,0,-1):
#     print(i)

#wap to print multiplication table of number n
# n = int(input("Enter a number for table:"))
# for i in range(1,11):
#     print(n,"*",i,"=",n*i)

#pass statements
# for i in range(5):
#     pass # it will do nothing 
# print("do some work")

#practice question 
#wap to find sum of first n numbers (in while loop)
# n = int(input("Enter a number:"))
# i = 1
# sum = 0
# while(i<=n):
#     sum += i
#     i += 1
# print(sum)
#in for loop
# for i in range(1,n+1):
#     sum += i
# print(sum)

#wap to find factorial of n number
# num = int(input("To find factorial enter a number:"))
# factorial = 1
# for i in range(1,num+1):
#     factorial *= i
# print(factorial)
#with while loop
# i = 1
# while(i<=num):
#     factorial *= i
#     i += 1 
# print(factorial)


