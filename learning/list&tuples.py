# marks = [93.2, 84.3, 84.6, 78.6, 92, 88, 48.5]
# print(marks)
# print(type(marks))
# print(len(marks))
# print(marks[0])
# print(type(marks[2]))
# print(type(marks[4]))

#we can change valuse in list 
# student = ["pratik",8.45,19,"Bantwa"]
# print(student[3])
# student[3] = "Ahemdabad"
# print(student)

#list same as strings many functions of strings can work on list 
#like slice method 
# marks = [93.2, 84.3, 84.6, 78.6, 92, 88, 48.5]
# print(marks[1:4])
# print(marks[4:1])
# print(marks[-4:-1])

#Method's in list 
# marks = [2, 5, 3, 4, 7, 7, 1]
# marks.append(5)#add a value in the end 
# marks.sort() #sorts in acending order ,this methods also can work on strings list
# marks.sort(reverse=True) #sorts in decending order
# marks.reverse()#it reverse the whall list
# marks.insert(2,'p')#it insert a new value on idx 2, it don't replace old value it just insert new value
# marks.remove(7)#this method remove value at first occurance
# marks.pop(3)#it removes perticular value of index 3
# print(marks)    

#practice on insert method
# student = []
# student.insert(0,input("Enter your name:"))
# student.insert(1,int(input("Enter your age:")))
# student.insert(2,int(input("Enter your password:")))
# student.insert(3,input("Enter your city:"))
# print(student)

#Tuple in python
# tup = (2,3,1,5)
# print(tup)
# print(type(tup))
# print(tup[0])
# print(tup[1])
# tup[0] = 5 #we can't change a value in tuple like strings(means it is immutable)

# tup = (1,)#write a ',' is important because if don't write it python will take a our value as a int
# #for example we don't write ","
# tup1 = (1)
# # print(tup)
# print(tup1)
# # print(type(tup))
# print(type(tup1))

#to print empty tuple
# tup = ()
# print(tup)
# print(type(tup))

#sliceing is same as strings and lists
# tup = (1,4,3,5,6)
# print(type(tup))
# print(tup[0:4])

#methods in tuple 
# tup = (1,4,3,5,6,3,4,4)
# print(tup)
# print(tup.index(3))#3 is a value and this method find what is the index of 3
# # print(tup.index(2))#it will show error because in our tuple there is no such value 2
# print(tup.count(4))#this method find how many time our value it repete's 

#practice questions
#wap to ask user to enter name of 3 favorite movies and store them in list
# movies = []
# print("Enter your 3 favorite movie name.")
# movies.insert(0,input("1)"))
# movies.insert(1,input("2)"))
# movies.insert(2,input("3)"))
# print(movies)
# #or
# movies.append(input("1)"))
# movies.append(input("2)"))
# movies.append(input("3)"))
# print(movies)
#or
# mov1 = input("1)")
# mov2 = input("2)")
# mov3 = input("3)")
# movies.append(mov1)
# movies.append(mov2)
# movies.append(mov3)
# print(movies)

#wap to check is list is palindrome or not. (use copy method)
# list = [1,2,3,2,1]
# R_list = list.copy()
# R_list.reverse()
# if(list == R_list):
#     print("This list is palindrome list.")
# else:
#     print("This list is not palindrome.")

#wap to count the number of student with "A" grade 
# grades = ("C","D","A","A","B","B","A")
# print(grades.count("A"))

#wap to store the above tuple in new list and print them in acending order
# grades = ["C","D","A","A","B","B","A"]
# grades.sort()
# print(grades)

a = "Parmar Pratik"
print(a.islower())