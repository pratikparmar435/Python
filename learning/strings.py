# different types to write a strings in python
# str1 = "This is a string."
# str2 = 'Tony Stark'
# str3 = '''Parmar Pratik'''
# str4 = """This is python"""
# print(str1,"\n",str2,"\n",str3,"\n",str4)

# why we need different strings methods
#Example
# str = "This is apnaCollege's tutorial."

#Operations on strings
#Concatenates
# str1 = "Parmar"
# str2 = "pratik"
# print(str1 +" "+ str2)
# #length
# print(len(str1))
# print(len(str2))

#indexing in python 
# str = "I am Parmar Pratik"
# ch = str[0]
# print(ch)#output will be I 
# #or
# print(str[5])#The output will be P
# str[2] = "@" #We can't change character's of strings with indexing

#Slice method of strings
# str = "Apna College"
# print(str[0:5])#The char. 5th index will no be included.The output will be 'Apna'
# print(str[5:12])#The output will be 'college'
# #or
# print(str[5:len(str)])#The output will be 'college'
# #or
# print(str[5:])#This will go to ending of the string and the output will be 'college'
# #or
# #if we have to print string form starting to out needed index then
# print(str[:4])#the output will be 'apna'

#Negitive indexing 
# str = "apple"
# print(str[-3:-1])#the output will be 'pl',because in negitive indexing idexing 
# #starts from ending -1 to start character
# print(str[-5:-2])#the output will be 'app'.just like normal indexing in this the character of -2 index will not be included

#Method's in strings
# str = "tony stark"
# print(str.endswith("ark"))#return true if the string ends with substring
# print(str.capitalize())#capitalize 1st character
# print(str.replace("t","P"))#use to replace any characters in our string or any word with other word
# #or
# str1 = input("Enter your name: ")
# print(str1.replace("pratik","khushi"))
# print(str1.capitalize())
# print(str1)#the above two function createa a new string they don't affect the original string
# #if we want to change the original string we need to write a like this 
# str1 = str1.capitalize()
# print("string after intializing actual value of function")
# str1 = str1.replace("pratik","khushi")
# print(str1)
#find function  
# str = "I am studying python from Apnacollege"
# print(str.find("o"))#returns 1st index of 1st occurrer
# print(str.find("am"))
# print(str.find("pm"))#if no character found then it returns -1.but nagitive index is only use for sliceing method 
#count fuction in strings
# str = "I am studying python from Apnacollege"
# print(str.count("e"))#this function counts how many times words is used in string
# print(str.count("from"))

#practice questions

# #WAP to input user's first name and print it's length
# f_name = input("Enter your first name: ")
# lgt_name = len(f_name)
# print("Length of your first name: ",lgt_name)

#WAP to print how many times $ occures in string
# str = "The $ has high rate in india then $ sign in america"
# print(str.count("$"))

#wap to check if string is palindrome or not
str = input("Enter a string to check it is palindrome or not:")


