student = {}

#adding student
def addStudent(name,grade):
    student[name] = grade
    print(f"{name} is added with marks {grade}")

#updating student
def updateStudent(name,grade):
    if name in student.keys():
        student[name] = grade
        print(f"{name} with marks are updated {grade}")
    else:
        print(f"student with name {name} not found!")

#delete student
def deleteStudent(name):
    if name in student.keys():
        del student[name]
        print(f"{name} has been successfully deleted")
    else:
        print(f"student with name {name} not found!")

#view all the student
def viewAllStudent():
    if student:
        for name,grade in student.items():
            print(f"{name} : {grade}")
        else:
            print("No student found!")

def main():
    while True:
        print("\n Student Grade Management System ")
        print("1. Add Student")
        print("2. Update Student")
        print("3. Delete Student")
        print("4. View All Student")
        print("5. Exit")

        choice = int(input("Enter your choice number ="))
        if choice == 1:
            name = input("Enter student name =")
            grade = int(input("Enter student grade ="))
            addStudent(name,grade)
        
        elif choice == 2:
            name = input("Enter student name =")
            grade = int(input("Enter updated student grade ="))
            updateStudent(name,grade)
        
        elif choice == 3:
            name = input("Enter student name =")
            deleteStudent(name)
        
        elif choice == 4:
            viewAllStudent()

        elif choice == 5:
            print("Closing the program")
            break

        else:
            print("No command found!")
main()

            

