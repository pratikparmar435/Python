# f = open(r"C:\Users\Dhaval Parmar\Desktop\pratik\python\learning\demo.txt","a")

# data = f.read()
# print(data)

# line1 = f.readline()
# print(line1)

# line2 = f.readline()
# print(line2)

# line3 = f.readline()
# print(line3)

# line4 = f.readline()
# print(line4)

# f.write("\nThen i'll move to ReactJs.")
# f.write(" and then nodejs")

# f.close()

# n = open("sample.txt","w")
# n.write("This will create new file automatically")
# n.close()

# d = open("sample.txt",'r+')

# d.write('that')

# d.close()

#With Syntax
# with open("sample.txt","r") as f:
#     data = f.read()
#     print(data)
    #No need to close file in with syntax

# with open("sample.txt","w") as d:
#     d.write("new data")

#module to delete any file 
# import os
# os.remove("sample.txt")

#practice question
# with open("practice.txt","r") as f:
#     data = f.read()

# new_data = data.replace("Java","Python")
# print(new_data)

# with open("practice.txt","w") as d:
#     d.write(new_data)

#check if learning word is in our file or not

# with open("practice.txt","r") as f:
#     data = f.read()
#     if(data.find("learning") != -1):
#         print("Found")
#     else:
#         print("Not Found")

#find the line number where this word found
# def find_line():
#     with open("practice.txt",'r') as f:
#         word = "learning"
#         data = True
#         line_no = 1
#         while data:
#             data = f.readline()
#             if(word in data):
#                 print(line_no)
#                 return
#             line_no += 1
#     return -1

# find_line()

# with open("practice.txt","r") as f:
#     data = f.read()
#     # num = ""
#     # for i in range(len(data)):
#     #     if data[i] == ",":
#     #         print(int(num))
#     #         num = ""
#     #     else:
#     #         num += data[i]
#     #or
#     count = 0
#     nums = data.split(",")
#     for val in nums:
#         if int(val) % 2 == 0:
#             count += 1 
# print(count)

# def read_file():
#     with open("practice.txt","r") as f:
#         print(f.read())
# read_file()

# import pickle

# # Create a Python dictionary
# data = {"name": "Alice", "age": 25, "skills": ["Python", "Machine Learning"]}

# # Open a file in binary write mode
# with open("data.pkl", "wb") as file:
#     pickle.dump(data, file)  # Serialize the dictionary and save it to the file

# print("Data serialized and saved to 'data.pkl'")



    
