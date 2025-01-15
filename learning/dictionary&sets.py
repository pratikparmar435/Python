#Sample example of dictionary
# info = {
#     "key" : "value",
#     "name" : "pratik",
#     "learning" : "python",
#     "age" : 22,
#     "is_sdult" : True,
#     "marks" : 8.45
# }
# print(info)

#we can also store list and tuples in our dictionary
# info = {
#     "name" : "pratik",
#     "subjects" : ["python", "java", "flutter", "ui/ux"],
#     "topics" : ("dictionary", "sets"),
#     "age" : 22,
#     "is_sdult" : True,
#     "marks" : 8.45
# }
# print(info)
# print(type(info))
# print(info["name"])
# #dictionary is mutable means we can change values in key and also can add a new key:value pair
# info["name"] = "Divya"
# info["surname"] = "Godhaniya"#adding new key:pair value
# print(info)

#In dictionary our key can be any of data type expect list 
# because list is mutable means it can be cange but tuple can be a key in our dictionary.
# student = {
#     "name" : "pratik",#string key
#     22 : "age", #int key
#     8.45 : "cgpa",#float key
#     True : "is_adult",#bool key
#     ("dict","sets") : "topic"
# }
# print(student)

#creating a null dictionary
# null_dict = {}#valid
# print(null_dict)
# print("After adding new key value pair:")
# null_dict["name"] = "Parmar Pratik"#adding new key value pair to our null dictionary
# print(null_dict)

#nested dictionary
# student = {
#     "name" : "parmar pratik",
#     "subjects" : {
#         "php" : 59,
#         "cpp" : 89,
#         "py" : 76,
#     },
#     "age" : 20
# }
# print(student)
# print(student["subjects"])
# print(student["subjects"]["cpp"])#find specific key under nest dict

#mehods in dictionary
# student = {
#     "name" : "parmar pratik",
#     "subjects" : {
#         "php" : 59,
#         "cpp" : 89,
#         "py" : 76,
#     },
#     "age" : 20
# }
# print(student.keys())#nested keys will be not printed
# print(len(student))#counts total pairs in dict
# print(list(student.keys()))#print keys in form of list
# print(len(list(student.keys())))#print length of our list 

# print(student.values())#in nested dict all keys and values considers as values of one subject key
# print(list(student.values()))#prints our values in form of list
# print(len(student.values()))#prints count of our values in dict

# print(student.items())#prints whall key:value pairs in form of tuples 
# print(list(student.items()))#converts tuples in list
#or
# pairs = list(student.items())#we can print endividual pairs with this
# print(pairs[0])
# print(pairs[1])

# print(student["name"])
# print(student.get("name"))

# student.update({"city" : "dehli"})
# print(student)

#SETS
# collection = {1,2,3,4,"Hello","world"}
# print(collection)
# print(type(collection))
#sets must contain unique value duplicate values not allowed
# set2 = {1,2,2,"Hello","world","world",4}#also set is unordered,it will ignore duplicate values
# print(set2)
# print(len(set2))#even if we print length of our set it will ignore duplicate items

#create a empty set
# collection = {} # this syntax is use create a empty dictionary not a set
# print(type(collection))
# collection = set() # this is valid syntax to create a empty set
# print(type(collection))

#Method's of Set's in python
# collection = set()
#1)
# collection.add(1)#adds value in set
# collection.add(2)
# collection.add(2)#set will ignore this value
# collection.add("pratik")#we can add string
# collection.add((1,2,3,4))#can add tuple
# collection.add([3,4,5,2,4])#can't add list and dict because they are mutable,
#set is also mutable but it's always contains immutable values
#2)
# print(collection)
# collection.remove(2)#it removes both 2 and only 1 remains in our set
# print(collection)
#3)
# print(len(collection))
# collection.clear()#it will make our set empty
# print(len(collection))
#4)
# collection = {"HEllo", "apnacollege", "world","coding","python"}
# print(collection.pop())#randomly print any value 
# print(collection.pop())#output will be not same to last time
#5)
# set1 = {1,2,3}
# set2 = {3,4,5}
# print(set1.union(set2))#combine two sets and gaves unique set
# print(set1)
# print(set2)
# print(set1.intersection(set2))#print common value between them 

#practice question
#wap to store given values in dictionary
# meaning_dict = {
#     cat : "a small animal",
#     table : ["a piece of furniture","list of facts & figures"]
# }

#wap to find how many class will needed for each subjects
# subject = {"python","java","c++","python","javascript","java","python","java","c++","c"}
# print(len(subject))
# print(subject)

#wap to take input a marks of 3 subject and store them in a dictionary
marks = {}

# x = int(input("Enter marks of py:"))
# marks.update({"py" : x})

# x = int(input("Enter marks of cpp:"))
# marks.update({"cpp" : x})

# x = int(input("Enter marks of js:"))
# marks.update({"js" : x})
# print(marks)
#or
# marks["py"] = int(input("Enter marks of py:"))
# marks["cpp"] = int(input("Enter marks of cpp:"))
# marks["js"] = int(input("Enter marks of js:"))
# print(marks)

#wap to store 9 and 9.0 in a set
# set1 = {9,9.0}
# print(set1)
# # or
# set2 = {9,"9.0"}
# print(set2)
# #or
# set3 = {("float",9.0),("int",9)}#create tuple inside a set
# print(set3)
