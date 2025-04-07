# import level4
# class demo:
#     x = 10
# obj = demo()#creating object for my demo class
# print(obj.x)

# class detail:
#     name = "pratik"
#     age = 20
#     def __init__(self):#this is constructor
#         print(f"name : {self.name}, age : {self.age}")
# std = detail()

# class A1:
#     x = 10
#     def sum(self):
#         x = 20
#         self.x += x
#         print(f"x from method of class: {x}")
#         print(f"x from class:{self.x}")
# o1 = A1()
# o1.sum()

# class demo2:
#     def __init__(self,name,age):
#         print(f"Name: {name},Age: {age}")
# std2 = demo2("Dhaval",21)

#inheritance
#parent class
# class Person:
#     def __init__(self,firstname,lastname):
#         self.firstname = firstname
#         self.lastname = lastname
    
#     def printname(self):
#         print(self.firstname,self.lastname)
#         print(f"{self.firstname} {self.lastname}")
#         print(self.age)

# #child class 
# class Student(Person):#this will inherits properties of person class 
#     def __init__(self,firstname,lastname,age):
#         self.firstname = firstname
#         self.lastname = lastname
#         self.age = age

# std1 = Student("Narendra","Modi",55)
# std1.printname()
# print(md.string)

#Creating user defined Exception 
class NegativeNumberError(Exception):
    pass
# def chkNum(num):
#     if num<0:
#         raise NegativeNumberError("Negative numbers are not allowed")
#     else:
#         print("valid number:",num)
# try: 
#     n = int(input("Enter a number:"))
#     chkNum(n)
# except NegativeNumberError as e:
#     print("Error : ",e)
#or 
# try:
#     n = int(input("Enter a number:"))
#     if n<0:
#         raise NegativeNumberError("Negative numbers are not allowed")
#     print("all set!")
# except NegativeNumberError as e:
#     print("Error :",e)     

# import tkinter as tk
# from tkinter import messagebox
# # Function to display message
# def show_message():
#     messagebox.showinfo("Info", "Button Clicked!")
# # Function to get text from Entry
# def get_text():
#     text = entry.get()
#     label.config(text=f"Hello, {text}")
# # Main Window
# root = tk.Tk()
# root.title("Complete Tkinter GUI")
# root.geometry("400x400")
# # Label
# label = tk.Label(root, text="Welcome to Tkinter GUI", font=("Arial", 14))
# label.pack(pady=5)
# # Entry Field (Text Input)
# entry = tk.Entry(root, width=30)
# entry.pack(pady=5)
# # Button
# button = tk.Button(root, text="Click Me", command=show_message)
# button.pack(pady=5)
# # Another Button to Get Text
# button2 = tk.Button(root, text="Submit Name", command=get_text)
# button2.pack(pady=5)
# # Text Area (Multi-line Input)
# text_area = tk.Text(root, height=5, width=40)
# text_area.pack(pady=5)
# # Listbox (Selectable Items)
# listbox = tk.Listbox(root)
# listbox.pack(pady=5)
# listbox.insert(1, "Option 1")
# listbox.insert(2, "Option 2")
# listbox.insert(3, "Option 3")
# # Canvas (Drawing Area)
# canvas = tk.Canvas(root, width=200, height=100, bg="lightgray")
# canvas.pack(pady=5)
# canvas.create_rectangle(50, 20, 150, 80, fill="red")
# # Menu Bar
# menu_bar = tk.Menu(root)
# root.config(menu=menu_bar)
# file_menu = tk.Menu(menu_bar, tearoff=0)
# file_menu.add_command(label="Open")
# file_menu.add_command(label="Save")
# file_menu.add_separator()
# file_menu.add_command(label="Exit", command=root.quit)
# menu_bar.add_cascade(label="File", menu=file_menu)
# # Run the application
# root.mainloop()

#checking factorial number
# n = int(input("Enter a number:"))
# fact = 1
# for i in range(2,n+1):
#     fact *= i
# print(fact)

#fibonacci series with recursion 
# def fibonacciNum(n):
#     if n == 0:
#         return "Invalid input"
#     elif n == 1:
#         return 0
#     elif n == 2:
#         return 1
#     else:
#         return fibonacciNum(n-1) + fibonacciNum(n-2)
# for i in range(1,6):
#     print(fibonacciNum(i),end=" ")

#fibonacci series with loops
# n = 5
# a = 0 
# b = 1
# print(f"Fibonacci sequence up to {n} terms:")
# for i in range(n):
#     print(a,end=" ")
#     temp = a
#     a = b
#     b = temp+b

#sum of 1 to N with while loop 
# n = int(input("Enter a number:"))
# i = 1
# sum = 0
# while i<=n:
#     sum += i
#     i += 1
# print(sum)

#factorial of number using recursion 
# def findFact(n):
#     if n == 1:
#         return 1
#     return findFact(n-1) * n
# print(findFact(3))

# import tkinter as tk
# root = tk.Tk()
# root.title("Simple Tkinter Example")
# l1 = tk.Label(root,text="username:")
# l1.pack()
# entry = tk.Entry(root)
# entry.pack(pady=10)
# button = tk.Button(root, text="Submit")
# button.pack(pady=5)
# label = tk.Label(root, text="Output will be shown here")
# label.pack(pady=5)
# root.mainloop()

import tkinter as tk
# Create the main application window
root = tk.Tk()
root.title("Listbox Example")  # Set window title
root.geometry("300x250")  # Set window size
# Create a Listbox widget
listbox = tk.Listbox(root, height=5, width=20)  # Set listbox size
listbox.pack(pady=10)  # Add vertical padding for better layout
# Define a list of items
options = ["Python", "Java", "C++", "JavaScript", "Swift"]
# Insert items into the Listbox
for option in options:
    listbox.insert(tk.END, option)  # Add each item at the END of the list
# Run the Tkinter main loop
root.mainloop()
